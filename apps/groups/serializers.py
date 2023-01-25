from rest_framework.serializers import ModelSerializer

from apps.groups.models import GroupModel
from apps.orders.serializers import OrderSerializer


class GroupSerializer(ModelSerializer):

    class Meta:
        model = GroupModel
        fields = ('id', 'name')
