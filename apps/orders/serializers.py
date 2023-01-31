from rest_framework.serializers import ModelSerializer

from apps.groups.serializers import GroupSerializer

from .models import CommentModel, OrderModel


class CommentSerializer(ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ('id', 'comment', 'created_at')
        read_only_fields = ('id', 'created_at')


class OrderSerializer(ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    group = GroupSerializer()

    class Meta:
        model = OrderModel
        fields = ('id', 'name', 'surname', 'email', 'phone', 'age', 'course', 'course_format', 'course_type',
                  'alreadyPaid', 'sum', 'msg', 'status', 'manager', 'created_at', 'utm', 'comments', 'group')
        read_only_fields = ('id', 'created_at', 'utm', 'manager')
        depth = 1


class OrderEditSerializer(OrderSerializer):
    group = None
