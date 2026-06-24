from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class User(AbstractUser):
    """Extended User model with email as primary identifier."""

    ROLE_CHOICES = (
        ('RESEARCHER', _('Researcher')),
        ('COMPANY_ADMIN', _('Company Admin')),
        ('TRIAGE_LEAD', _('Triage Lead')),
        ('ADMIN', _('Platform Admin')),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, db_index=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='RESEARCHER')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'auth_user'
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['role']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip() or self.email


class Profile(models.Model):
    """User profile with additional metadata."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # Profile info
    avatar_url = models.URLField(blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, default='')
    location = models.CharField(max_length=100, blank=True, default='')
    website = models.URLField(blank=True, null=True)

    # 2FA
    two_fa_enabled = models.BooleanField(default=False)
    two_fa_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, blank=True, default='')

    # Privacy
    hide_email = models.BooleanField(default=False)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'accounts_profile'
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
        ordering = ['-created_at']

    def __str__(self):
        return f"Profile of {self.user.email}"


class TwoFactorAuthentication(models.Model):
    """2FA TOTP secret storage."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='two_fa_auth')

    # TOTP secret (encrypted in production)
    secret_key = models.CharField(max_length=255)
    backup_codes = models.JSONField(default=list)  # List of backup codes

    # Status
    is_enabled = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_used = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'accounts_2fa'
        verbose_name = _('Two Factor Authentication')
        verbose_name_plural = _('Two Factor Authentications')

    def __str__(self):
        return f"2FA for {self.user.email}"


class PasswordReset(models.Model):
    """Password reset token storage."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='password_resets')

    token = models.CharField(max_length=255, unique=True)
    used = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    class Meta:
        db_table = 'accounts_password_reset'
        verbose_name = _('Password Reset')
        verbose_name_plural = _('Password Resets')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['token']),
            models.Index(fields=['user', 'used']),
        ]

    def __str__(self):
        return f"Reset for {self.user.email}"


class UserSession(models.Model):
    """Track active user sessions."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sessions')

    # Session info
    token = models.CharField(max_length=500, unique=True)
    device_info = models.CharField(max_length=255, blank=True)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField(blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    last_activity = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'accounts_session'
        verbose_name = _('User Session')
        verbose_name_plural = _('User Sessions')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'is_active']),
            models.Index(fields=['token']),
        ]

    def __str__(self):
        return f"Session of {self.user.email}"


class EmailVerification(models.Model):
    """Email verification tokens."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='email_verifications')
    
    token = models.CharField(max_length=255, unique=True)
    is_verified = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    class Meta:
        db_table = 'accounts_email_verification'
        verbose_name = _('Email Verification')
        verbose_name_plural = _('Email Verifications')
        ordering = ['-created_at']

    def __str__(self):
        return f"Email Verification for {self.user.email}"


class SecurityEvent(models.Model):
    """Audit log for security events."""

    EVENT_CHOICES = (
        ('LOGIN', _('Login Successful')),
        ('FAILED_LOGIN', _('Login Failed')),
        ('LOGOUT', _('Logout')),
        ('PASSWORD_CHANGE', _('Password Changed')),
        ('PASSWORD_RESET', _('Password Reset')),
        ('2FA_ENABLED', _('2FA Enabled')),
        ('2FA_DISABLED', _('2FA Disabled')),
        ('ACCOUNT_DEACTIVATED', _('Account Deactivated')),
        ('ACCOUNT_REACTIVATED', _('Account Reactivated')),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='security_events', null=True, blank=True)
    
    event_type = models.CharField(max_length=50, choices=EVENT_CHOICES)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    metadata = models.JSONField(default=dict, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'accounts_security_event'
        verbose_name = _('Security Event')
        verbose_name_plural = _('Security Events')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.event_type} - {self.user.email if self.user else 'Unknown'}"


class Invitation(models.Model):
    """Invitations for users to join."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    role = models.CharField(max_length=20, choices=User.ROLE_CHOICES, default='RESEARCHER')
    
    token = models.CharField(max_length=255, unique=True)
    invited_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='invitations_sent')
    
    is_accepted = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    class Meta:
        db_table = 'accounts_invitation'
        verbose_name = _('Invitation')
        verbose_name_plural = _('Invitations')
        ordering = ['-created_at']

    def __str__(self):
        return f"Invitation to {self.email} ({self.role})"
