from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from cameo.models import Cameo
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Booking
import random
import json
# Create your views here.


def book(request,username):
    if request.method == 'GET':
        cameo = get_object_or_404(Cameo, username=username)
        context ={
            "cameo": cameo
        }
        return render(request, 'booking/book.html', context=context)

@api_view(['POST'])
def create_booking(request):
    if request.user.is_authenticated:
        cameo = get_object_or_404(Cameo, id=request.POST.get('cameo_id'))
        from_user = request.POST.get('from')
        to_user = request.POST.get('to')
        occasion = request.POST.get('occasion')
        receipent = request.POST.get('receipent')
        instructions = request.POST.get('instructions')
        hide_cameo = request.POST.get('hideCameo')
        pronounce = request.POST.get('pronounce')
        order_id = random.randint(1,1000000)
        request_user_id = request.user.id
        request_user_username = request.user.username
        cameo_id = cameo.id
        cameo_username = cameo.username
        order_status = 'initiated'
        payment_method = 'paypal'
        payment_status = 'initiated'
        price = cameo.price
        currency_code = cameo.currency_code
        new_booking = Booking(order_id=order_id, price=price, currency_code=currency_code, cameo_id=cameo_id, cameo_username=cameo_username,requested_user_id=request_user_id, requested_user_username=request_user_username, fromName=from_user, toName=to_user,pronounce=pronounce, instructions=instructions,occasion=occasion,receipent=receipent, payment_status=payment_status, payment_method=payment_method, payment_server_response='[]', order_status=order_status)
        new_booking.save()
        return Response({"detail": request.POST, 'order_id': order_id})
    else:
        return Response(request.POST)

def payment_process(request, order_id):
    booking = get_object_or_404(Booking, order_id=order_id)
    context= {"booking":booking}
    return render(request, 'booking/payment.html', context=context)