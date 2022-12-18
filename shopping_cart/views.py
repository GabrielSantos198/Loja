from django.shortcuts import render, redirect
from cart.cart import Cart
from products.models import Product

# Create your views here.
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    return render(request, 'cart/cart_detail.html')


def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect('cart:cart_detail')


def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('cart:cart_detail')


def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product=product)
    return redirect('cart:cart_detail')
