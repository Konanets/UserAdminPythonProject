from django.urls import path

from apps.groups.views import GroupsListCreateView

urlpatterns = [
    path('', GroupsListCreateView.as_view()),
]