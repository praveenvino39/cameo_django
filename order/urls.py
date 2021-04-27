from django.urls import path
from . import views

urlpatterns = [
    path("send/<int:order_id>", view=views.send_cameo, name="send_cameo"),
    path("accept/<int:order_id>", view=views.accept, name="accept"),
]
