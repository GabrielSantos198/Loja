from django.shortcuts import render, redirect
from django.conf import settings
from django.views import View
from cart.cart import Cart
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        cart_products = Cart(request).session['cart']
        total = 0
        for cart, number in enumerate(cart_products):
            total += int(cart_products[number]['quantity']) * float(cart_products[number]['price'])
        total = total * 100
        YOUR_DOMAIN = 'https://thunderstore.herokuapp.com'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data':{
                        'currency':'brl',
                        'unit_amount': int(total),
                        'product_data':{
                            'name': 'Thunder Store',
                        },
                    },
                    'quantity':1,
                }
            ],
                mode='payment',
                success_url=YOUR_DOMAIN + f'/create/order/client/{kwargs["id"]}',
                cancel_url=YOUR_DOMAIN + '/cancel',
            )
        return redirect(checkout_session.url, code=303)

