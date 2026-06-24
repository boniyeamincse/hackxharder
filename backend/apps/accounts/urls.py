from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from . import views

app_name = 'accounts'

urlpatterns = [
    # Core Auth
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh-token'),
    path('me/', views.UserProfileView.as_view(), name='me'),
    
    # Email Verification
    path('email/verify/', views.EmailVerifyView.as_view(), name='email-verify'),
    path('email/resend-verification/', views.EmailResendVerificationView.as_view(), name='email-resend'),
    
    # Passwords
    path('password-reset/', views.PasswordResetRequestView.as_view(), name='password-reset'),
    path('password-reset-confirm/', views.PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('password/change/', views.ChangePasswordView.as_view(), name='password-change'),
    
    # Tokens
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),
    
    # Sessions & Devices
    path('sessions/', views.SessionListView.as_view(), name='sessions'),
    path('sessions/<uuid:session_id>/revoke/', views.SessionRevokeView.as_view(), name='session-revoke'),
    path('devices/', views.SessionListView.as_view(), name='devices'),
    path('devices/<uuid:session_id>/revoke/', views.SessionRevokeView.as_view(), name='device-revoke'),
    
    # 2FA
    path('2fa/setup/', views.TwoFactorSetupView.as_view(), name='2fa-setup'),
    path('2fa/verify/', views.TwoFactorVerifyView.as_view(), name='2fa-verify'),
    path('login/2fa/', views.Login2FAVerifyView.as_view(), name='login-2fa'),
    path('2fa/disable/', views.TwoFactorDisableView.as_view(), name='2fa-disable'),
    path('2fa/recovery-codes/', views.TwoFactorRecoveryCodesView.as_view(), name='2fa-recovery-codes'),
    path('2fa/recovery-codes/regenerate/', views.TwoFactorRegenerateRecoveryCodesView.as_view(), name='2fa-recovery-codes-regen'),
    
    # Audit & Security Events
    path('login-history/', views.LoginHistoryView.as_view(), name='login-history'),
    path('security-events/', views.SecurityEventListView.as_view(), name='security-events'),
    
    # Account Lifecycle
    path('account/deactivate/', views.AccountDeactivateView.as_view(), name='account-deactivate'),
    path('account/reactivate/', views.AccountReactivateView.as_view(), name='account-reactivate'),
    path('account/delete-request/', views.AccountDeleteRequestView.as_view(), name='account-delete-request'),
    
    # Roles & Permissions
    path('role/', views.UserRoleView.as_view(), name='role'),
    path('permissions/', views.UserPermissionsView.as_view(), name='permissions'),
    
    # Invitations
    path('invite/accept/', views.InviteAcceptView.as_view(), name='invite-accept'),
    path('invite/verify/', views.InviteVerifyView.as_view(), name='invite-verify'),
]
