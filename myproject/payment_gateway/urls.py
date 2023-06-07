from django.urls import path
from . import views

app_name = 'payment_gateway'

urlpatterns = [
    path('', views.payment, name='payment'),
    # Add more URLs as needed
]
