from django.contrib import admin
from . models import Item, Order

# Register your models here.
class ItemInline(admin.TabularInline):
    model = Item
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'cpf', 'cep', 'state', 'created', 'is_sent']
    list_filter = ['is_sent']
    search_fields = ['name']
    inlines = [ItemInline]
