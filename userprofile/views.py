from django.shortcuts import render
from django.http import HttpResponse
from booking.models import Booking
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def sales(request):
    sales = Booking.objects.filter(cameo=request.user)
    sales = sales.filter(payment_status="completed")
    context = {"sales": sales}
    return render(request, "userprofile/sales.html", context=context)


@login_required
def purchase(request):
    purchase = Booking.objects.filter(requested_user_id=request.user.id)
    purchase = purchase.filter(payment_status="completed")
    context = {"purchases": purchase}
    return render(request, "userprofile/purchase.html", context=context)
