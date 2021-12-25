from json.decoder import JSONDecoder
from django.contrib.auth.models import User
from django.http import request, response
import json

from django.utils import translation
import cameo
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from .models import Cameo, CameoSerializer
from django.views.decorators.csrf import csrf_exempt
from django.db.models.expressions import RawSQL
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cameoproject.response_helper import send_response
from rest_framework import status

# Create your views here.


def homepage(request):
    cameos = []
    results = Cameo.objects.all()
    for cameo in results:
        if len(cameo.reviews) >= 6 and cameo.username != request.user.username:
            cameos.append(cameo)
    context = {"categories": Cameo.category_choice, "cameos": cameos}
    return render(request, "cameo/homepage.html", context=context)


def login_view(request):
    print(request.GET.get("next"))
    context = {"next": request.GET.get("next")}
    return render(request, "cameo/login_page.html", context=context)


def login_user(request):
    if request.method == "POST":
        user = Cameo.objects.filter(username=request.POST.get("username")).first()
        if user:
            if user.check_password(request.POST.get("password")):
                login(request=request, user=user)
                token, created = Token.objects.get_or_create(user=user)
                messages.success(request, token.key, extra_tags="authentication")
                if request.GET.get("next"):
                    return redirect("{}".format(request.GET.get("next")))
                else:
                    return redirect("homepage")
            else:
                messages.error(
                    request, "Username or Password invalid.", extra_tags="danger"
                )
                return redirect("login_page")
        else:
            messages.error(
                request, "Username or Password invalid.", extra_tags="danger"
            )
            return redirect("login_page")
    else:
        return redirect("homepage")


def logout_user(request):
    logout(request=request)
    return redirect("homepage")


def show_cameo(request, username):
    cameo = get_object_or_404(Cameo, username=username)
    context = {"cameo": cameo, "review_count": len(cameo.reviews)}
    return render(request, "cameo/show_cameo.html", context=context)


@api_view(["POST"])
def login_api(request):
    if request.method == "POST":
        user = Cameo.objects.filter(username = request.data.get("username")).first()
        if user is not None:
            if user.check_password(request.data.get("password")):
                login(request=request, user=user)
                token, created = Token.objects.get_or_create(user=user)
                messages.success(request, token.key, extra_tags="authentication")
                user = CameoSerializer(user)
                return send_response(data={"token": str(token), "user": user.data},isSuccess=True,code=status.HTTP_200_OK)
            else:
                return send_response(isSuccess=False,code=status.HTTP_400_BAD_REQUEST, message="Username or password invalid")
        else:
            return send_response(isSuccess=False,code=status.HTTP_404_NOT_FOUND, message="Username or password invalid")



@api_view(["GET"])
def homepage_api(request):
    most_reviewed = []
    results = Cameo.objects.filter(is_celebrity = True)
    for cameo in results:
        if len(most_reviewed) == 0:
            if len(cameo.reviews) >= 6 and cameo.username != request.user.username:
                most_reviewed.append(cameo)
        else:
            if len(cameo.reviews) >= len(most_reviewed[0].reviews) and cameo.username != request.user.username:
                most_reviewed.insert(0,cameo)
    most_reviewed = CameoSerializer(most_reviewed, many=True)
    trending_cameo = Cameo.objects.filter(is_celebrity = True).order_by('-fans')
    trending_cameo = CameoSerializer(trending_cameo, many=True)
    new_cameo = Cameo.objects.filter(is_celebrity = True).order_by("-date_joined")
    new_cameo = CameoSerializer(new_cameo, many=True)
    return send_response(code=status.HTTP_200_OK, isSuccess=True, data={"category": Cameo.category_choice, "most_reviewed":  most_reviewed.data[:10], "trending":trending_cameo.data[:10], "new": new_cameo.data})