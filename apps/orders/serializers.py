from rest_framework.serializers import ModelSerializer

from apps.groups.models import GroupModel

from .models import CommentModel, OrderModel


class CommentSerializer(ModelSerializer):
    class Meta:
        order = CommentModel
        field = ('id', 'comment', 'created_at')
        read_only_fields = ('id', 'created_at')


class OrderSerializer(ModelSerializer):
    comments = CommentSerializer(many=True)
    group = GroupModel()

    class Meta:
        model = OrderModel
        fields = ('__all__',)
        read_only_fields = ('id', 'manager', 'alreadyPaid', 'created_at', 'utm')
