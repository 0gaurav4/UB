from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    # Add more URLs as needed
]
