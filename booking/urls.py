from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path('<str:username>', views.book, name='book'),
    path('create-booking/', views.create_booking, name='create-booking'),
    path('start/<int:order_id>', views.payment_process,
         name='payment-process'),
    path('payment/stripe',
         views.stripe_payment_create,
         name="stripe-payment-create"),
    path('start/create-checkout-session/<int:order_id>',
         views.stripe_token,
         name="stripe token"),
    path('verify', views.verify_stripe, name="stripe-payment-verify"),
]