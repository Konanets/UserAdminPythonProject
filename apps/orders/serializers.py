from rest_framework.serializers import ModelSerializer

from apps.groups.serializers import GroupSerializer
from apps.users.serializers import ProfileSerializer

from .models import CommentModel, OrderModel


class CommentSerializer(ModelSerializer):
    manager = ProfileSerializer(read_only=True)

    class Meta:
        model = CommentModel
        fields = ('id', 'comment', 'created_at', 'order_id', 'manager')
        read_only_fields = ('id', 'created_at', 'order_id')


class OrderSerializer(ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    group = GroupSerializer()

    class Meta:
        model = OrderModel
        fields = ('id', 'name', 'surname', 'email', 'phone', 'age', 'course', 'course_format', 'course_type',
                  'alreadyPaid', 'sum', 'msg', 'status', 'manager', 'created_at', 'utm', 'comments', 'group')
        read_only_fields = ('id', 'created_at', 'utm', 'manager', 'msg')
        depth = 1


class OrderEditSerializer(OrderSerializer):
    group = None

    class Meta:
        model = OrderModel
        fields = ('id', 'name', 'surname', 'email', 'phone', 'age', 'course', 'course_format', 'course_type',
                  'alreadyPaid', 'sum', 'msg', 'status', 'manager', 'created_at', 'utm', 'comments', 'group')
        read_only_fields = ('id', 'created_at', 'utm', 'manager', 'msg')
        depth = 0
