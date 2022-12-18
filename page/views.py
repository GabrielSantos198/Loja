from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from . models import AboutPage
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
class AboutPageView(ListView):
    queryset = AboutPage.objects.all().order_by('-modified')[0:1]
    context_object_name = 'about'
    template_name = 'about.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def post(self, request):
        organize = (f"nome: {request.POST['name']}\ne-mail: {request.POST['email']}\nmessage: {request.POST['message']}")
        send_mail(
            subject=request.POST['subject'],
            message=organize,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )
        return render(request, 'success.html')

