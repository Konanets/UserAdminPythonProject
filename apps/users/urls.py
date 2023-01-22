from django.urls import path

from apps.users.views import MyView

urlpatterns = [
    path('/my', MyView.as_view()),
]