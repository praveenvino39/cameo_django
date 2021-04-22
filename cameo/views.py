from django.http import request
import json
import cameo
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from .models import Cameo
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token

# Create your views here.


def homepage(request):
    cameos = []
    results = Cameo.objects.all()
    for cameo in results:
        if len(cameo.reviews) >= 6:
            cameos.append(cameo)
    context = {'categories': Cameo.category_choice, 'cameos': cameos}
    return render(request, 'cameo/homepage.html', context=context)


def login_view(request):
    return render(request, 'cameo/login_page.html')


def login_user(request):
    if request.method == "POST":
        user = Cameo.objects.filter(
            username=request.POST.get('username')).first()
        if user:
            login(request=request, user=user)
            token, created = Token.objects.get_or_create(user=user)
            messages.success(request, token.key, extra_tags='authentication')
            return redirect('homepage')
        else:
            messages.error(request,
                           'Username or Password invalid.',
                           extra_tags="danger")
            return redirect('login_page')
    else:
        return redirect('homepage')


def logout_user(request):
    logout(request=request)
    return redirect('homepage')


def show_cameo(request, username):
    cameo = get_object_or_404(Cameo, username=username)
    context = {"cameo": cameo, "review_count": len(cameo.reviews)}
    return render(request, 'cameo/show_cameo.html', context=context)