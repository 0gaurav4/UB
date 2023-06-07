from django.urls import path
from . import views

app_name = 'notification'

urlpatterns = [
    path('', views.notifications, name='notifications'),
    # Add more URLs as needed
]
