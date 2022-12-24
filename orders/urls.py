from django.urls import path
from . views import create_order

app_name = 'client_orders'

urlpatterns = [
    path('order/client/<int:id>/', create_order, name='create_order'),
]
