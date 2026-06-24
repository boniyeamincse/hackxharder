from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile, TwoFactorAuthentication, PasswordReset, UserSession


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Admin for User model."""

    fieldsets = (
        (None, {'fields': ('id', 'email', 'password')}),
        ('Personal Info', {'fields': ('username', 'first_name', 'last_name')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Role', {'fields': ('role',)}),
        ('Important Dates', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )

    list_display = ('email', 'username', 'role', 'is_active', 'created_at')
    list_filter = ('role', 'is_active', 'created_at')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('-created_at',)
    readonly_fields = ('id', 'created_at', 'updated_at', 'last_login')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'role'),
        }),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Admin for Profile model."""

    list_display = ('user', 'location', 'two_fa_enabled', 'created_at')
    list_filter = ('two_fa_enabled', 'created_at')
    search_fields = ('user__email', 'location')
    readonly_fields = ('id', 'user', 'created_at', 'updated_at')

    fieldsets = (
        ('User', {'fields': ('id', 'user')}),
        ('Profile Info', {'fields': ('avatar_url', 'bio', 'location', 'website')}),
        ('2FA', {'fields': ('two_fa_enabled', 'two_fa_verified', 'phone_number')}),
        ('Privacy', {'fields': ('hide_email',)}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )


@admin.register(TwoFactorAuthentication)
class TwoFactorAuthenticationAdmin(admin.ModelAdmin):
    """Admin for 2FA model."""

    list_display = ('user', 'is_enabled', 'is_verified', 'created_at')
    list_filter = ('is_enabled', 'is_verified', 'created_at')
    search_fields = ('user__email',)
    readonly_fields = ('id', 'user', 'secret_key', 'created_at', 'updated_at', 'last_used')

    fieldsets = (
        ('User', {'fields': ('id', 'user')}),
        ('2FA Setup', {'fields': ('secret_key', 'backup_codes')}),
        ('Status', {'fields': ('is_enabled', 'is_verified')}),
        ('Activity', {'fields': ('created_at', 'updated_at', 'last_used')}),
    )


@admin.register(PasswordReset)
class PasswordResetAdmin(admin.ModelAdmin):
    """Admin for password reset tokens."""

    list_display = ('user', 'used', 'created_at', 'expires_at')
    list_filter = ('used', 'created_at')
    search_fields = ('user__email', 'token')
    readonly_fields = ('id', 'token', 'created_at')

    fieldsets = (
        ('Token Info', {'fields': ('id', 'token')}),
        ('User', {'fields': ('user',)}),
        ('Status', {'fields': ('used',)}),
        ('Expiry', {'fields': ('created_at', 'expires_at')}),
    )


@admin.register(UserSession)
class UserSessionAdmin(admin.ModelAdmin):
    """Admin for user sessions."""

    list_display = ('user', 'ip_address', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('user__email', 'ip_address')
    readonly_fields = ('id', 'token', 'created_at', 'last_activity')

    fieldsets = (
        ('Session Info', {'fields': ('id', 'token')}),
        ('User', {'fields': ('user',)}),
        ('Device Info', {'fields': ('device_info', 'ip_address', 'user_agent')}),
        ('Status', {'fields': ('is_active',)}),
        ('Activity', {'fields': ('created_at', 'expires_at', 'last_activity')}),
    )
