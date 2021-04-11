from django.http import request
import json
import cameo
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from .models import Cameo

# Create your views here.


def homepage(request):
    cameos = Cameo.objects.all()
    context = {'categories': Cameo.category_choice, 'cameos': cameos}
    return render(request, 'cameo/homepage.html', context=context)


def login_user(request):
    if request.method == "POST":
        user = Cameo.objects.filter(
            username=request.POST.get('username')).first()
        if user:
            login(request=request, user=user)
            return redirect('homepage')
        else:
            messages.error(request,
                           'Username or Password invalid.',
                           extra_tags="danger")
            return redirect('homepage')
    else:
        return redirect('homepage')


def logout_user(request):
    logout(request=request)
    return redirect('homepage')


def show_cameo(request, username):
    cameo = get_object_or_404(Cameo, username=username)
    context = {"cameo": cameo, "review_count": len(json.loads(cameo.reviews))}
    return render(request, 'cameo/show_cameo.html', context=context)