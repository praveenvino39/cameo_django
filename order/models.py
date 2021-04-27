from django.db import models
from booking.models import Booking

# Create your models here.


class File(models.Model):
    order = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name="file", null=True
    )
    cameo_file = models.FileField(upload_to="cameoFile")

    def __str__(self):
        return "{}".format(self.order_id)