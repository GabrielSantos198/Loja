from django.urls import path
from . views import AboutPageView, ContactPageView

app_name = 'page'

urlpatterns = [
    path('sobre/', AboutPageView.as_view(), name='about'),
    path('contato/', ContactPageView.as_view(), name='contact'),
]


