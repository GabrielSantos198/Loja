from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from . models import Product
from page.models import HomePageSlideShow, InstagramSection

# Create your views here.
class HomePageView(ListView):
    queryset = Product.objects.filter(featured=True)
    context_object_name = 'featured'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['HomePageSlideShow'] = HomePageSlideShow.objects.all().order_by('-modified')[0]
        context['InstagramSection'] = InstagramSection.objects.all().order_by('-modified')[0]
        return context


class ProductsPageView(ListView):
    queryset = Product.objects.filter(is_available=True).order_by('-modified')
    context_object_name = 'products'
    template_name = 'store.html'


class ProductDetailPageView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'detail.html'
