from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import File
from rest_framework import status
from booking.models import Booking

# Create your views here.


@api_view(["POST"])
def send_cameo(request, order_id):
    if request.user.is_authenticated:
        cameo_file = request.FILES.get("cameoFile")
        if (
            cameo_file.name.endswith(".mp4")
            or cameo_file.name.endswith(".avi")
            or cameo_file.name.endswith(".mov")
            or cameo_file.name.endswith(".mkv")
        ):
            if cameo_file.size <= 10000000:
                booking = Booking.objects.filter(order_id=order_id).first()
                new_order = File(order=booking, cameo_file=cameo_file)
                new_order.save()
                booking.order_status = "Completed Request"
                booking.save()
                return Response({"status": True}, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"status": False, "error": "File size shouldn't exceed 10mb"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                {"status": False, "error": "File format not supported"},
                status=status.HTTP_400_BAD_REQUEST,
            )
    else:
        return Response(
            {"error": "Not authorized"}, status=status.HTTP_401_UNAUTHORIZED
        )


@api_view(["GET"])
def accept(request, order_id):
    if request.user.is_authenticated:
        booking = Booking.objects.filter(order_id=order_id).first()
        if booking.requested_user_id == request.user.id:
            booking.is_accepted = True
            booking.order_status = "Completed"
            booking.save()
            return Response(booking.is_accepted, status=status.HTTP_200_OK)
        else:
            return Response("you're not authorized to do this action")
    else:
        return Response(
            {"error": "Not authorized"}, status=status.HTTP_401_UNAUTHORIZED
        )


@api_view(["POST"])
def decline(request):
    if request.user.is_authenticated:
        booking = Booking.objects.filter(order_id=request.POST.get("order_id")).first()
        if booking.requested_user_id == request.user.id:
            booking.decline_reason = request.POST.get("reason")
            booking.save()
            return Response(booking.is_accepted, status=status.HTTP_200_OK)
        else:
            return Response("you're not authorized to do this action")
    else:
        return Response(
            {"error": "Not authorized"}, status=status.HTTP_401_UNAUTHORIZED
        )