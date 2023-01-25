from django.urls import path

from apps.groups.views import GroupsListView

urlpatterns = [
    path('', GroupsListView.as_view()),
]