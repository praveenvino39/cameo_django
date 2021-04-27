from .models import Cameo
from booking.models import Booking


def newsale_processor(request):
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(cameo=request.user)
        new_sale = []
        for booking in bookings:
            if booking.order_status != "completed":
                new_sale.append(booking)
        return {"new_sale": len(new_sale)}
    else:
        return {"new_sale": 0}


def purchase_update(request):
    if request.user.is_authenticated:
        purchase = []
        bookings = Booking.objects.filter(requested_user_id=request.user.id)
        for booking in bookings:
            if booking.order_status == "completed":
                purchase.append(booking)
        return {"purchase_update": len(purchase)}
    else:
        return {"purchase_update": 0}
