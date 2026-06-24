from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/v1/auth/', include('apps.accounts.urls', namespace='auth')),
    path('api/v1/researchers/', include('apps.researchers.urls', namespace='researchers')),
    path('api/v1/programs/', include('apps.companies.urls', namespace='programs')),
    path('api/v1/reports/', include('apps.reports.urls', namespace='reports')),
    path('api/v1/triage/', include('apps.triage.urls', namespace='triage')),
    path('api/v1/messages/', include('apps.messaging.urls', namespace='messages')),
    path('api/v1/payments/', include('apps.payments.urls', namespace='payments')),
    path('api/v1/admin/', include('apps.admin_panel.urls', namespace='admin')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    if 'django_debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
