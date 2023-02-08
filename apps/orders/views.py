from core.enums.choice_enum import StatusChoice
from core.pagination.page_pagination import PagePagination

from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, get_object_or_404
from rest_framework.response import Response

from apps.orders.filters import OrderFilter
from apps.orders.models import CommentModel, OrderModel
from apps.orders.serializers import CommentSerializer, OrderEditSerializer, OrderSerializer
from apps.users.models import ProfileModel

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

parameters = [
    openapi.Parameter('my', openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN),
    openapi.Parameter('order', openapi.IN_QUERY, 'example: "id" asc or "-id" desc', type=openapi.TYPE_BOOLEAN),
    openapi.Parameter('start_date', openapi.IN_QUERY, 'example: ?start_date=2020-01-01', type=openapi.TYPE_STRING),
    openapi.Parameter('end_date', openapi.IN_QUERY, 'example: ?end_date=2022-01-01', type=openapi.TYPE_STRING),
]


@method_decorator(name='get', decorator=swagger_auto_schema(manual_parameters=parameters))
class OrdersListView(ListAPIView):
    serializer_class = OrderSerializer
    queryset = OrderModel.objects.all()
    pagination_class = PagePagination
    filterset_class = OrderFilter

    def get_queryset(self):
        qs = self.queryset.all()
        my = self.request.query_params.get('my')

        if my == 'true':
            qs = qs.filter(manager__user_id__exact=self.request.user.pk)

        return qs


class OrderRetrieveUpdateView(GenericAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer

    def get_serializer_class(self):

        if self.request.method == 'PATCH':
            return OrderEditSerializer

        if self.request.method == 'GET':
            return OrderSerializer



    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = get_object_or_404(OrderModel, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = get_object_or_404(OrderModel, pk=pk)
        data: dict = self.request.data

        if not data.get('status'):
            order.status = StatusChoice.IN_WORK

        order.manager = None if data.get('status') == StatusChoice.NEW else ProfileModel.objects.get(
            user_id=self.request.user.pk)

        serializer = OrderEditSerializer(order, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)


class OrderCommentsListView(GenericAPIView):
    serializer_class = CommentSerializer
    queryset = CommentModel.objects.all()

    def get(self, *args, **kwargs):
        order_id = kwargs.get('order_id')
        comments = CommentModel.objects.filter(order_id=order_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        order_id = kwargs.get('order_id')
        data = self.request.data
        order = OrderModel.objects.all().get(pk=order_id)

        serializer = CommentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(order_id=order)

        if not order.manager:
            order.manager = ProfileModel.objects.get(user_id=self.request.user.pk)
            order.save()

        return Response(serializer.data, status.HTTP_200_OK)
