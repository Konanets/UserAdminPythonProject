from core.services.jwt_service import ActivateToken, JWTService, Token

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainSerializer, TokenRefreshSerializer
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.auth.serializers import PasswordSerializer

from drf_yasg.utils import swagger_auto_schema


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Login
    """
    serializer_class = TokenObtainSerializer

    @swagger_auto_schema(responce={status.HTTP_200_OK: TokenObtainSerializer}, security=[])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomTokenRefreshView(TokenRefreshView):
    """
    Refresh
    """
    serializer_class = TokenRefreshSerializer

    @swagger_auto_schema(responce={status.HTTP_200_OK: TokenRefreshSerializer}, security=[])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


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
