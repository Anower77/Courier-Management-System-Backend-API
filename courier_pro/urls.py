from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Courier Management API",
      default_version='v1',
      description="API endpoints for Users, Admins, Delivery Men",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('accounts.urls')),
    path('api/v1/orders/', include('courier_app.urls')),

    # Swagger/OpenAPI
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
