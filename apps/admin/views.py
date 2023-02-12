from core.services.jwt_service import ActivateToken, JWTService

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.users.models import UserModel
from apps.users.serializers import UserSerializer


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all().filter(is_superuser=False)
    permission_classes = (IsAdminUser,)


class CreateUserTokenView(GenericAPIView):

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')

        user = get_object_or_404(UserModel, pk=pk)
        token = JWTService.create_token(user, ActivateToken)

        return Response(str(token), status.HTTP_201_CREATED)
