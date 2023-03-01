from django.urls import path

from apps.auth.views import ActivateUserAccountView, CustomTokenObtainPairView, CustomTokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', TokenObtainPairView.as_view()),
    path('/refresh', TokenRefreshView.as_view()),
    path('/activate/<str:token>', ActivateUserAccountView.as_view())
]
