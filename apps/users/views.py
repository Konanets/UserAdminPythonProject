from typing import Type

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer

UserModel: Type[User] = get_user_model()


class MyView(GenericAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user

    def get(self, *args, **kwargs):
        serializer = UserSerializer(self.get_object())
        return Response(serializer.data, status.HTTP_200_OK)
