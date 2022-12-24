from django.db import models
from model_utils.models import TimeStampedModel
from localflavor.br.models import BRStateField

# Create your models here.
class Order(TimeStampedModel):
    username = models.CharField(max_length=100)
    cpf = models.CharField('CPF', blank=False, max_length=11)
    cep = models.CharField('CEP', blank=False, max_length=8)
    state = BRStateField('State', blank=False)
    city = models.CharField(max_length=150, blank=False)
    address = models.CharField(max_length=150, blank=False)
    district = models.CharField(max_length=150, blank=False)
    number = models.CharField(max_length=50, blank=False)
    complement = models.CharField(max_length=150, blank=False)
    is_sent = models.BooleanField(default=False)


    class Meta:
        ordering = ['-created']


    def __str__(self):
        return f'{self.username} Order'


class Item(TimeStampedModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.FloatField(max_length=10)
