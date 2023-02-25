from django.urls import path

from apps.admin.views import CreateUserTokenView, UserListCreateView, StatisticsByManagerView, StatisticsByOrdersView, \
    BanUserView, UnBanUserView

urlpatterns = [
    path('/users', UserListCreateView.as_view()),
    path('/users/<int:pk>/re_token', CreateUserTokenView.as_view()),
    path('/statistic/users/<int:pk>', StatisticsByManagerView.as_view()),
    path('/statistic/orders', StatisticsByOrdersView.as_view()),
    path('/users/<int:pk>/ban', BanUserView.as_view()),
    path('/users/<int:pk>/unban', UnBanUserView.as_view()),
]
