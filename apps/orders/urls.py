from django.urls import path

from apps.orders.views import OrderRetrieveUpdateView, OrdersListView

urlpatterns = [
    path('', OrdersListView.as_view()),
    path('/<int:pk>', OrderRetrieveUpdateView.as_view())
]
