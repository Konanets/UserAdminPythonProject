from django.urls import path

from apps.admin.views import CreateUserTokenView, UserListCreateView

urlpatterns = [
    path('/users', UserListCreateView.as_view()),
    path('/users/<int:pk>/re_token', CreateUserTokenView.as_view())
]
