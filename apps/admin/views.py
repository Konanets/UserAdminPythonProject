from core.pagination.page_pagination import PagePagination
from core.services.jwt_service import ActivateToken, JWTService

from django.db.models import Count
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer
from apps.orders.models import OrderModel

from abc import ABC, abstractmethod
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

UserModel: User = get_user_model()


class AdminTools(GenericAPIView, ABC):
    permission_classes = IsAdminUser,

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.id)

    @abstractmethod
    def patch(self, *args, **kwargs):
        pass


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all().filter(is_superuser=False)
    permission_classes = (IsAdminUser,)
    pagination_class = PagePagination


class CreateUserTokenView(GenericAPIView):
    """
    get some token: qwohoiboqiwbgieurbgbqierguqrbgoqbrubg
    """

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')

        user = get_object_or_404(UserModel, pk=pk)
        token = JWTService.create_token(user, ActivateToken)

        return Response(str(token), status.HTTP_201_CREATED)


class StatisticsByManagerView(GenericAPIView):
    queryset = UserModel.objects.filter(is_superuser=False)
    permission_classes = IsAdminUser,

    def get(self, *args, **kwargs):
        total_count = OrderModel.objects.filter(manager__user=self.kwargs.get('pk')).count()

        statuses = OrderModel.objects.filter(manager__user=self.kwargs.get('pk')).values('status').annotate(
            count=Count('id'))

        statistics = {
            'total_count': total_count,
            'statuses': statuses
        }

        return Response(statistics)


class StatisticsByOrdersView(GenericAPIView):
    permission_classes = IsAdminUser,

    def get(self, *args, **kwargs):
        total_count = OrderModel.objects.all().count()

        statuses = OrderModel.objects.values('status').annotate(count=Count('id'))

        statistics = {
            'total_count': total_count,
            'statuses': statuses,
        }

        return Response(statistics)


class BanUserView(AdminTools):
    serializer_class = UserSerializer

    def patch(self, *args, **kwargs):
        user: User = self.get_object()

        if user.is_active:
            user.is_active = False
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UnBanUserView(AdminTools):
    serializer_class = UserSerializer

    def patch(self, *args, **kwargs):
        user: User = self.get_object()

        if not user.is_active:
            user.is_active = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)
