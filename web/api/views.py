from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

import stripe
from rest_framework.decorators import api_view
from .models import Item, Order
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def item(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, 'details.html', {'order': order, 'settings': settings})


@api_view(['GET'])
def buy(request, order_id):
    order = Order.objects.get(id=order_id)
    items = order.items.all()
    line_items = []
    for item in items:
        line_items.append({
            "price_data": {
                "currency": "usd",
                "product_data": {
                    "name": item.name
                },
                "unit_amount": int(item.price * 100),
            },
            "quantity": 1,
        })

    if order.tax:
        line_items.append({
            "price_data": {
                "currency": "usd",
                "product_data": {
                    "name": "Tax"
                },
                "unit_amount": int(order.tax.tax_amount * 100),
            },
            "quantity": 1,
        })

    discounts = None
    if order.discount:
        discounts = [{
            'coupon': stripe.Coupon.create(amount_off=int(order.discount.discount_amount * 100),
                                           duration="once",
                                           currency='usd')
        }]

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        mode="payment",
        discounts=discounts,
        success_url=f"http://localhost:8000/success",
        cancel_url="http://localhost:8000/cancel",
    )

    return JsonResponse({"session_id": session.id})


def cancel(request):
    return render(request, 'cancel.html')


def success(request):
    return render(request, 'success.html')

