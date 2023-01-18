from django.urls import path

from apps.orders.views import OrderRetrieveView, OrdersListView

urlpatterns = [
    path('', OrdersListView.as_view()),
    path('/<int:pk>', OrderRetrieveView.as_view())
]
