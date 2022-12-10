from django.urls import path
from . views import HomePageView, ProductsPageView, ProductDetailPageView

app_name = 'products'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('produtos/', ProductsPageView.as_view(), name='products'),
    path('<slug:slug>/', ProductDetailPageView.as_view(), name='product_detail'),
]

