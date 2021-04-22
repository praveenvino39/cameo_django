from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
import stripe
import json
from booking.models import Booking
from cameo.models import Cameo

# Create your views here.


def start_stripe(request, order_id):
    if request.method == 'GET':
        booking = get_object_or_404(Booking, order_id=order_id)
        context = {"booking": booking}
        return render(request, 'booking/payment.html', context=context)
    elif request.method == 'POST':
        booking = get_object_or_404(Booking, order_id=order_id)
        context = {"booking": booking}
        return render(request,
                      'payment/stripe_payment_create.html',
                      context=context)


@api_view(['POST'])
def stripe_token(request, order_id):
    stripe.api_key = 'sk_test_InNmafpyVmRe0re1YqIYvHEm006Sztmcf0'
    try:
        booking = get_object_or_404(Booking, order_id=order_id)
        service_fee = (booking.price / 100) * 5
        cameo = get_object_or_404(Cameo, id=booking.cameo_id)
        price = booking.price + service_fee
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': "inr",
                        'unit_amount': int(price * 100),
                        'product_data': {
                            'name':
                            'Cameo from {} {}'.format(cameo.first_name,
                                                      cameo.last_name),
                            'images': [
                                "https://pbs.twimg.com/profile_images/1331393187185876993/o7dCt1PW_400x400.jpg"
                            ],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url="http://127.0.0.1:8000" + '/payment/stripe/success',
            cancel_url="http://127.0.0.1:8000" + '/cancel.html',
        )
        request.session["transaction_id"] = booking.order_id
        return Response(data={'id': checkout_session.id})
    except Exception as e:
        return Response(data={'error': "error"})


def stripe_success(request):
    response = request.body
    booking = get_object_or_404(Booking,
                                order_id=request.session.get('transaction_id'))
    booking.payment_status = 'completed'
    booking.save()
    booking.payment_method = 'stripe'

    return render(request, 'payment/stripe_success.html')
