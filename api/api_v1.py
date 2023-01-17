from django.urls import include, path

urlpatterns = [
    path('/auth', include('apps.auth.urls')),
    path('/orders', include('apps.orders.urls'))
]