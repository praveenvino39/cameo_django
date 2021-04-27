from django.db import models
from cameo.models import Cameo

# Create your models here.


class Booking(models.Model):

    payment_method_choice = [("paypal", "Paypal"), ("stripe", "Stripe")]
    payment_status_choice = [
        ("initiated", "Initiated"),
        ("pending", "Pending"),
        ("completed", "Completed"),
    ]
    order_status_choice = [
        ("initiated", "Initiated"),
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("Completed Request", "Completed Request"),
    ]
    cameo = models.ForeignKey(
        Cameo, on_delete=models.CASCADE, related_name="cameo", null=True
    )
    order_id = models.IntegerField()
    # cameo_id = models.IntegerField()
    price = models.FloatField()
    currency_code = models.CharField(max_length=10)
    cameo_username = models.CharField(max_length=250)
    requested_user_id = models.IntegerField()
    requested_user_username = models.CharField(max_length=250)
    fromName = models.CharField(max_length=500, null=True, blank=True)
    toName = models.CharField(max_length=500)
    pronounce = models.CharField(max_length=500)
    instructions = models.TextField()
    occasion = models.CharField(max_length=500)
    receipent = models.CharField(max_length=500)
    payment_status = models.CharField(max_length=100, choices=payment_status_choice)
    payment_method = models.CharField(max_length=100, choices=payment_method_choice)
    payment_server_response = models.TextField()
    order_status = models.CharField(max_length=50, choices=order_status_choice)
    statisfaction = models.IntegerField(null=True, blank=True)
    is_accepted = models.BooleanField(default=False, null=True, blank=True)
    decline_reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.cameo_username