from django.urls import path

from apps.auth.views import ActivateUserAccountView, CustomTokenObtainPairView, CustomTokenRefreshView

urlpatterns = [
    path('', CustomTokenObtainPairView.as_view()),
    path('/refresh', CustomTokenRefreshView.as_view()),
    path('/activate/<str:token>', ActivateUserAccountView.as_view())
]
