from django.urls import path
from . import views


app_name = "book"

urlpatterns = [
    path('<str:username>', views.book, name='book'),
    path('create-booking/', views.create_booking, name='create-booking'),
    path('start/<int:order_id>', views.payment_process, name='payment-process')
]