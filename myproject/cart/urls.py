from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart, name='cart'),
    # Add more URLs as needed
]
