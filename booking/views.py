from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from cameo.models import Cameo

# Create your views here.


def book(request,username):
    cameo = get_object_or_404(Cameo, username=username)
    context ={
        "cameo": cameo
    }
    return render(request, 'booking/book.html', context=context)