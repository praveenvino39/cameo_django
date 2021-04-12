from django.urls import path
from . import views


app_name = "book"

urlpatterns = [
    path('<str:username>', views.book, name='book')
]