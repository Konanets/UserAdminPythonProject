from core.enums.choice_enum import StatusChoice
from core.pagination.page_pagination import PagePagination

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.db.models import Count

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, get_object_or_404
from rest_framework.response import Response

from apps.orders.filters import OrderFilter
from apps.orders.models import CommentModel, OrderModel
from apps.orders.serializers import CommentSerializer, OrderEditSerializer, OrderSerializer
from apps.users.models import ProfileModel

import xlwt
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

        if order.manager and order.manager.user_id != self.request.user.pk:
            return Response('not your order', status.HTTP_403_FORBIDDEN)

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
        manager = ProfileModel.objects.get(user_id=self.request.user.pk)

        if order.manager and order.manager.user_id != self.request.user.pk:
            return Response('not your order', status.HTTP_403_FORBIDDEN)

        if order.status != StatusChoice.IN_WORK:
            order.status = StatusChoice.IN_WORK
            order.save()

        serializer = CommentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(order_id=order, manager=manager)

        if not order.manager:
            order.manager = manager
            order.save()

        return Response(serializer.data, status.HTTP_200_OK)


class ExcelOrdersListView(GenericAPIView):
    serializer_class = OrderSerializer
    queryset = OrderModel.objects.all()
    filterset_class = OrderFilter

    def get(self, *args, **kwargs):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="orders.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Users Data')

        row_num = 0

        style = xlwt.XFStyle()

        font = xlwt.Font()
        font.bold = True
        font.colour_index = 56
        font.height = 400
        style.font = font

        borders = xlwt.Borders()
        borders.bottom = xlwt.Borders.DASHED
        style.borders = borders

        columns = ['id', 'name', 'surname', 'email', 'phone', 'age', 'status', 'course',
                   'course_type', 'course_format', 'manager', 'group']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], style=style)

        ws.col(0).width = 3000
        ws.col(1).width = 5000
        ws.col(2).width = 5000
        ws.col(3).width = 7000
        ws.col(4).width = 6000
        ws.col(5).width = 3000
        ws.col(6).width = 7000
        ws.col(7).width = 4000
        ws.col(8).width = 7000
        ws.col(9).width = 9000
        ws.col(10).width = 7000
        ws.col(11).width = 6000

        style = xlwt.XFStyle()
        style.font.height = 250

        cts_list = OrderModel.objects.all()
        cta_filter = OrderFilter(self.request.GET, queryset=cts_list)
        rows = cta_filter.qs.values_list('id', 'name', 'surname', 'email', 'phone', 'age', 'status',
                                         'course',
                                         'course_type', 'course_format', 'manager__name',
                                         'group__name')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], style=style)

        wb.save(response)

        return response


class StatisticsByOrders(GenericAPIView):
    def get(self, *args, **kwargs):
        total_count = OrderModel.objects.all().count()

        statuses = OrderModel.objects.values('status').annotate(count=Count('id'))

        statistics = {
            'total_count': total_count,
            'statuses': statuses,
        }

        return Response(statistics)
