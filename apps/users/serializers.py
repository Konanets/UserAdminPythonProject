from typing import Type

from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework.serializers import ModelSerializer

from apps.orders.serializers import OrderSerializer
from apps.users.models import ProfileModel
from apps.users.models import UserModel as User

UserModel: Type[User] = get_user_model()


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('name', 'surname')


class UserSerializer(ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'is_active', 'is_superuser', 'create_at', 'update_at', 'last_login', 'orders',
            'profile')
        read_only_fields = (
            'id', 'crated_at', 'update_at', 'is_superuser', 'last_login', 'is_active', 'orders')

    @transaction.atomic()
    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user
