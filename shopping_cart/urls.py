from django.urls import path
from . import views

app_name = 'cart' 

urlpatterns = [
    path('add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart-detail/', views.cart_detail, name='cart_detail'),
    path('item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart_clear/', views.cart_clear, name='cart_clear'),
]
