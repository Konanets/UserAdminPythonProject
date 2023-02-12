from typing import Type

from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework.serializers import ModelSerializer

from apps.users.models import ProfileModel
from apps.users.models import UserModel as User

UserModel: Type[User] = get_user_model()


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'user')
        read_only_fields = ('user',)


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'is_active', 'is_superuser', 'is_staff', 'create_at', 'update_at', 'last_login', 'profile')
        read_only_fields = (
            'id', 'crated_at', 'update_at', 'is_superuser', 'last_login', 'is_active')

    @transaction.atomic()
    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        return user
