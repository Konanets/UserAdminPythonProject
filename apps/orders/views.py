from core.pagination.page_pagination import PagePagination

from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.orders.filters import OrderFilter
from apps.orders.models import OrderModel
from apps.orders.serializers import OrderSerializer


class OrdersListView(ListAPIView):
    serializer_class = OrderSerializer
    queryset = OrderModel.objects.all()
    pagination_class = PagePagination
    filterset_class = OrderFilter

    def get_queryset(self):
        print(self.request.user.id)
        qs = self.queryset.all()
        my = self.request.query_params.get('my')

        if my:
            qs = qs.filter(manager__user_id__exact=self.request.user.pk)

        return qs


class OrderRetrieveView(RetrieveAPIView):
    serializer_class = OrderSerializer
    queryset = OrderModel.objects.all()
