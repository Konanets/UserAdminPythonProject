from django.urls import include, path

from rest_framework.permissions import AllowAny

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('/auth', include('apps.auth.urls')),
    path('/orders', include('apps.orders.urls')),
    path('/users', include('apps.users.urls')),
    path('/groups', include('apps.groups.urls')),
    path('/admin', include('apps.admin.urls')),
    path('/doc', schema_view.with_ui('swagger', cache_timeout=0)),
]
