from rest_framework.generics import ListAPIView

from apps.orders.serializers import OrderSerializer
from apps.orders.models import OrderModel

from core.pagination.page_pagination import PagePagination


class OrdersListView(ListAPIView):
    serializer_class = OrderSerializer
    queryset = OrderModel.objects.all()
    pagination_class = PagePagination
