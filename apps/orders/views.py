from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from serializers import OrderSerializer


class OrdersListView(ListAPIView):
    serializer_class = OrderSerializer()
    permission_classes = AllowAny,
