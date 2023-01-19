from core.pagination.page_pagination import PagePagination

from django.utils.decorators import method_decorator

from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.orders.filters import OrderFilter
from apps.orders.models import OrderModel
from apps.orders.serializers import OrderSerializer

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

        if my:
            qs = qs.filter(manager__user_id__exact=self.request.user.pk)

        return qs


class OrderRetrieveView(RetrieveAPIView):
    serializer_class = OrderSerializer
    queryset = OrderModel.objects.all()
