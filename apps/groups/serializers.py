from rest_framework.serializers import ModelSerializer

from apps.groups.models import GroupModel
from apps.orders.serializers import OrderSerializer


class GroupSerializer(ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        object = GroupModel
        fields = ('id', 'name', 'orders')
