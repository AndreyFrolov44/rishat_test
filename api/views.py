from django.shortcuts import render

import stripe
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def item(request, item_id):
    item = Item.objects.get(pk=item_id)
    return render(request, 'details.html', {'item': item, 'settings': settings})


@api_view(['GET'])
def buy(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": item.name,
                        "description": item.description
                    },
                    "unit_amount": int(item.price) * 100,
                },
                "quantity": 1,
            },
        ],
        mode="payment",
        success_url='http://localhost:8000/pay/success',
        cancel_url='http://localhost:8000/pay/cancel',
    )
    return Response({'session_id': session.id})


def cancel(request):
    return render(request, 'cancel.html')


def success(request):
    return render(request, 'success.html')

