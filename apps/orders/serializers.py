from rest_framework.serializers import ModelSerializer

from apps.groups.models import GroupModel

from .models import CommentModel, OrderModel


class CommentSerializer(ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ('id', 'comment', 'created_at')
        read_only_fields = ('id', 'created_at')


class OrderSerializer(ModelSerializer):
    comments = CommentSerializer(many=True)
    group = GroupModel()

    class Meta:
        model = OrderModel
        fields = ('id', 'name', 'surname', 'email', 'phone', 'age', 'course', 'course_format', 'course_type', 'manager',
                  'alreadyPaid', 'sum', 'msg', 'status', 'manager', 'created_at', 'utm', 'group', 'comments')
        read_only_fields = ('id', 'manager', 'alreadyPaid', 'created_at', 'utm')
