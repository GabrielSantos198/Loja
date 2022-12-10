from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from . models import AboutPage


# Create your views here.
class AboutPageView(ListView):
    queryset = AboutPage.objects.all().order_by('-modified')[0:1]
    context_object_name = 'about'
    template_name = 'about.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'
