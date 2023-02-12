from core.services.jwt_service import ActivateToken, JWTService

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.auth.serializers import PasswordSerializer


class ActivateUserAccountView(GenericAPIView):
    serializer_class = PasswordSerializer
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        data = self.request.data
        token = kwargs.get('token')

        serializer = PasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        user = JWTService.validate_token(token, ActivateToken)
        user.set_password(serializer.data.get('password'))
        user.is_active = True
        user.is_staff = True
        user.save()

        return Response(status=status.HTTP_200_OK)
