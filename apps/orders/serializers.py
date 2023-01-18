from rest_framework.serializers import ModelSerializer

from .models import CommentModel, OrderModel


class CommentSerializer(ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ('id', 'comment', 'created_at')
        read_only_fields = ('id', 'created_at')


class OrderSerializer(ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = OrderModel
        fields = ('id', 'name', 'surname', 'email', 'phone', 'age', 'course', 'course_format', 'course_type',
                  'alreadyPaid', 'sum', 'msg', 'status', 'manager', 'created_at', 'utm', 'comments', 'group')
        read_only_fields = ('id', 'alreadyPaid', 'created_at', 'utm')
        depth = True
