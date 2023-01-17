from typing import Type

from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework.serializers import ModelSerializer

from apps.users.models import UserModel as User

UserModel: Type[User] = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'email', 'password', 'is_active', 'is_superuser', 'create_at', 'update_at', 'last_login')
        read_only_fields = (
            'id', 'crated_at', 'update_at', 'is_superuser', 'last_login', 'is_active')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    @transaction.atomic()
    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user
