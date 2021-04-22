from .models import Cameo
from booking.models import Booking


def newsale_processor(request):
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(cameo=request.user)
        new_sale = []
        for booking in bookings:
            if booking.order_status != "completed":
                new_sale.append(booking)
        return {'new_sale': len(new_sale)}
    else:
        return {'new_sale': 0}
