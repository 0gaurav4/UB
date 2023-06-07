from django.urls import path
from . import views

app_name = 'order_management'

urlpatterns = [
    path('', views.order_management, name='order_management'),
    # Add more URLs as needed
]
