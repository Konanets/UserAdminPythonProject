from rest_framework.generics import ListCreateAPIView

from apps.groups.models import GroupModel
from apps.groups.serializers import GroupSerializer


class GroupsListCreateView(ListCreateAPIView):
    serializer_class = GroupSerializer
    queryset = GroupModel.objects.all()
