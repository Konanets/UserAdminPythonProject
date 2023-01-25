from rest_framework.generics import ListAPIView

from apps.groups.models import GroupModel
from apps.groups.serializers import GroupSerializer


class GroupsListView(ListAPIView):
    serializer_class = GroupSerializer
    queryset = GroupModel.objects.all()
