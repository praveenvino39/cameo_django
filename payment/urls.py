from django.urls import path
from . import views

urlpatterns = [
    path('start/stripe/<int:order_id>',
         views.start_stripe,
         name='start-stripe-payment'),
    path('stripe/token/<int:order_id>',
         views.stripe_token,
         name='stripe-token'),
    path('stripe/success', views.stripe_success, name='stripe-success'),
]
