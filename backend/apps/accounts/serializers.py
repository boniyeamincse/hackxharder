from rest_framework import serializers
from django.contrib.auth import authenticate
from django.utils.timezone import now
from datetime import timedelta
import uuid

from .models import User, Profile, TwoFactorAuthentication, PasswordReset, UserSession, EmailVerification, SecurityEvent, Invitation


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model."""

    class Meta:
        model = User
        fields = [
            'id', 'email', 'username', 'first_name', 'last_name',
            'role', 'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for Profile model."""

    user_email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id', 'user_email', 'avatar_url', 'bio', 'location', 'website',
            'two_fa_enabled', 'phone_number', 'hide_email', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'two_fa_enabled', 'created_at', 'updated_at']


class UserDetailSerializer(serializers.ModelSerializer):
    """Detailed user serializer with profile."""

    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'username', 'first_name', 'last_name',
            'role', 'is_active', 'profile', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""

    password = serializers.CharField(write_only=True, min_length=12)
    password2 = serializers.CharField(write_only=True, min_length=12)
    role = serializers.ChoiceField(
        choices=User.ROLE_CHOICES,
        default='RESEARCHER'
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2', 'role', 'first_name', 'last_name']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})

        # Password complexity
        password = attrs['password']
        if not any(char.isdigit() for char in password):
            raise serializers.ValidationError({
                'password': 'Password must contain at least one digit.'
            })
        if not any(char.isupper() for char in password):
            raise serializers.ValidationError({
                'password': 'Password must contain at least one uppercase letter.'
            })
        if not any(char.isalpha() for char in password):
            raise serializers.ValidationError({
                'password': 'Password must contain at least one letter.'
            })

        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()

        # Create profile
        Profile.objects.create(user=user)
        TwoFactorAuthentication.objects.create(user=user)

        return user


class LoginSerializer(serializers.Serializer):
    """Serializer for user login."""

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        # Authenticate
        user = authenticate(username=email, password=password)
        if not user:
            raise serializers.ValidationError('Invalid email or password.')

        if not user.is_active:
            raise serializers.ValidationError('This account is inactive.')

        attrs['user'] = user
        return attrs


class PasswordResetRequestSerializer(serializers.Serializer):
    """Serializer for password reset request."""

    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError('User with this email does not exist.')
        return value


class PasswordResetConfirmSerializer(serializers.Serializer):
    """Serializer for password reset confirmation."""

    token = serializers.CharField()
    password = serializers.CharField(write_only=True, min_length=12)
    password2 = serializers.CharField(write_only=True, min_length=12)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})

        token = attrs.get('token')
        try:
            reset = PasswordReset.objects.get(token=token, used=False)
            if reset.expires_at < now():
                raise serializers.ValidationError({'token': 'Reset link has expired.'})
        except PasswordReset.DoesNotExist:
            raise serializers.ValidationError({'token': 'Invalid reset token.'})

        attrs['reset'] = reset
        return attrs


class TwoFactorSetupSerializer(serializers.Serializer):
    """Serializer for 2FA setup (generate secret)."""

    pass


class TwoFactorVerifySerializer(serializers.Serializer):
    """Serializer for 2FA verification."""

    code = serializers.CharField(min_length=6, max_length=6)


class Login2FAVerifySerializer(serializers.Serializer):
    """Serializer for 2FA verification during login."""

    user_id = serializers.UUIDField()
    code = serializers.CharField(min_length=6, max_length=6)


class ChangePasswordSerializer(serializers.Serializer):
    """Serializer for changing password."""

    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True, min_length=12)
    new_password2 = serializers.CharField(write_only=True, min_length=12)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password2']:
            raise serializers.ValidationError({'new_password': 'Passwords do not match.'})
        return attrs


class UserSessionSerializer(serializers.ModelSerializer):
    """Serializer for user sessions."""

    class Meta:
        model = UserSession
        fields = [
            'id', 'ip_address', 'device_info', 'user_agent',
            'created_at', 'last_activity', 'is_active'
        ]
        read_only_fields = fields


class EmailVerifySerializer(serializers.Serializer):
    """Serializer for email verification."""
    token = serializers.CharField()


class EmailResendSerializer(serializers.Serializer):
    """Serializer to resend email verification."""
    email = serializers.EmailField()


class SecurityEventSerializer(serializers.ModelSerializer):
    """Serializer for security events/login history."""
    
    class Meta:
        model = SecurityEvent
        fields = ['id', 'event_type', 'ip_address', 'user_agent', 'metadata', 'created_at']
        read_only_fields = fields


class InvitationVerifySerializer(serializers.Serializer):
    """Serializer to verify an invitation token."""
    token = serializers.CharField()


class InvitationAcceptSerializer(serializers.Serializer):
    """Serializer to accept an invitation and set password."""
    token = serializers.CharField()
    password = serializers.CharField(write_only=True, min_length=12)
    password2 = serializers.CharField(write_only=True, min_length=12)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})
        return attrs
