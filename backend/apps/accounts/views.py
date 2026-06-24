from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from django.utils.timezone import now
from django.contrib.auth import authenticate
from datetime import timedelta
import pyotp
import qrcode
from io import BytesIO
import base64
import uuid

from .models import User, Profile, TwoFactorAuthentication, PasswordReset, UserSession
from .serializers import (
    UserSerializer, UserDetailSerializer, ProfileSerializer,
    RegisterSerializer, LoginSerializer,
    PasswordResetRequestSerializer, PasswordResetConfirmSerializer,
    TwoFactorSetupSerializer, TwoFactorVerifySerializer,
    ChangePasswordSerializer
)


class RegisterView(APIView):
    """Register new user."""

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserDetailSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """Login user and return JWT tokens."""

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']

            # Check if 2FA is enabled
            if user.profile.two_fa_enabled:
                return Response({
                    'message': '2FA is enabled. Verify with your authenticator.',
                    'requires_2fa': True,
                    'user_id': str(user.id),
                }, status=status.HTTP_200_OK)

            # Generate tokens
            refresh = RefreshToken.for_user(user)

            return Response({
                'user': UserDetailSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    """Logout user."""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Logout successful.'}, status=status.HTTP_200_OK)
        except TokenError:
            return Response(
                {'error': 'Invalid token.'},
                status=status.HTTP_400_BAD_REQUEST
            )


class TwoFactorSetupView(APIView):
    """Setup 2FA - generate secret and QR code."""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        two_fa = user.two_fa_auth

        # Generate secret
        secret = pyotp.random_base32()
        totp = pyotp.TOTP(secret)

        # Generate QR code
        uri = totp.provisioning_uri(
            name=user.email,
            issuer_name='HackXHarder'
        )
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(uri)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        qr_code = base64.b64encode(buffer.getvalue()).decode()

        return Response({
            'secret': secret,
            'qr_code': f'data:image/png;base64,{qr_code}',
            'uri': uri,
            'message': 'Scan QR code with authenticator app and verify with code.',
        }, status=status.HTTP_200_OK)


class TwoFactorVerifyView(APIView):
    """Verify 2FA code and enable 2FA."""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TwoFactorVerifySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = request.user
        code = serializer.validated_data['code']
        secret = request.data.get('secret')

        if not secret:
            return Response(
                {'error': 'Secret not provided. Call setup endpoint first.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Verify code
        totp = pyotp.TOTP(secret)
        if not totp.verify(code):
            return Response(
                {'error': 'Invalid 2FA code.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Enable 2FA
        two_fa = user.two_fa_auth
        two_fa.secret_key = secret
        two_fa.is_enabled = True
        two_fa.is_verified = True
        two_fa.save()

        user.profile.two_fa_enabled = True
        user.profile.two_fa_verified = True
        user.profile.save()

        # Generate backup codes
        backup_codes = [str(uuid.uuid4())[:8] for _ in range(10)]
        two_fa.backup_codes = backup_codes
        two_fa.save()

        return Response({
            'message': '2FA enabled successfully.',
            'backup_codes': backup_codes,
            'warning': 'Save backup codes in a secure location.',
        }, status=status.HTTP_200_OK)


class TwoFactorDisableView(APIView):
    """Disable 2FA."""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        code = request.data.get('code')

        if not user.profile.two_fa_enabled:
            return Response(
                {'error': '2FA is not enabled.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Verify current 2FA code
        two_fa = user.two_fa_auth
        totp = pyotp.TOTP(two_fa.secret_key)
        if not totp.verify(code):
            return Response(
                {'error': 'Invalid 2FA code.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Disable 2FA
        two_fa.is_enabled = False
        two_fa.is_verified = False
        two_fa.save()

        user.profile.two_fa_enabled = False
        user.profile.two_fa_verified = False
        user.profile.save()

        return Response(
            {'message': '2FA disabled successfully.'},
            status=status.HTTP_200_OK
        )


class PasswordResetRequestView(APIView):
    """Request password reset (send email)."""

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data['email']
        user = User.objects.get(email=email)

        # Create reset token
        token = str(uuid.uuid4())
        expires_at = now() + timedelta(hours=24)

        PasswordReset.objects.create(
            user=user,
            token=token,
            expires_at=expires_at
        )

        # TODO: Send email with reset link
        # For now, return token (unsafe for production)
        return Response({
            'message': 'Password reset email sent.',
            'token': token,  # Remove in production
        }, status=status.HTTP_200_OK)


class PasswordResetConfirmView(APIView):
    """Confirm password reset with token."""

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        reset = serializer.validated_data['reset']
        password = serializer.validated_data['password']

        user = reset.user
        user.set_password(password)
        user.save()

        reset.used = True
        reset.save()

        return Response({
            'message': 'Password reset successful. You can now login with your new password.',
        }, status=status.HTTP_200_OK)


class ChangePasswordView(APIView):
    """Change password (authenticated user)."""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = request.user
        old_password = serializer.validated_data['old_password']
        new_password = serializer.validated_data['new_password']

        # Verify old password
        if not user.check_password(old_password):
            return Response(
                {'error': 'Old password is incorrect.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(new_password)
        user.save()

        return Response({
            'message': 'Password changed successfully.',
        }, status=status.HTTP_200_OK)


class UserProfileView(APIView):
    """Get and update user profile."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserDetailSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user
        profile = user.profile

        # Update user fields
        user.first_name = request.data.get('first_name', user.first_name)
        user.last_name = request.data.get('last_name', user.last_name)
        user.save()

        # Update profile fields
        profile.bio = request.data.get('bio', profile.bio)
        profile.location = request.data.get('location', profile.location)
        profile.avatar_url = request.data.get('avatar_url', profile.avatar_url)
        profile.website = request.data.get('website', profile.website)
        profile.hide_email = request.data.get('hide_email', profile.hide_email)
        profile.save()

        serializer = UserDetailSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
