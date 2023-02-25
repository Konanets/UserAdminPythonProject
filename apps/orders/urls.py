from django.urls import path

from apps.orders.views import ExcelOrdersListView, OrderCommentsListView, OrderRetrieveUpdateView, OrdersListView

urlpatterns = [
    path('', OrdersListView.as_view()),
    path('/excel', ExcelOrdersListView.as_view()),
    path('/<int:pk>', OrderRetrieveUpdateView.as_view()),
    path('/<int:order_id>/comments', OrderCommentsListView.as_view()),
]
