from django.urls import path
from . views import AboutPageView, ContactPageView, ConfigPageView

app_name = 'page'

urlpatterns = [
    path('sobre/', AboutPageView.as_view(), name='about'),
    path('contato/', ContactPageView.as_view(), name='contact'),
    path('configuracao/', ConfigPageView.as_view(), name='config'),
]


