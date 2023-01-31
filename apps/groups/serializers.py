from rest_framework.serializers import ModelSerializer

from apps.groups.models import GroupModel


class GroupSerializer(ModelSerializer):

    class Meta:
        model = GroupModel
        fields = ('id', 'name')
