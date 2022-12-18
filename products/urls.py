from django.urls import path
from . views import HomePageView, ProductsPageView, ProductDetailPageView, ProductsCategoryView,  SearchResults

app_name = 'products'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('produtos/', ProductsPageView.as_view(), name='products'),
    path('<slug:slug>/', ProductDetailPageView.as_view(), name='product_detail'),
    path('produtos/categoria/<str:slug>/', ProductsCategoryView.as_view(), name='filter_products'),
    path('produtos/resultados/', SearchResults.as_view(), name='search_results'),
]

