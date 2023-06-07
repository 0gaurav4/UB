from django.urls import path
from . import views

app_name = 'feedback_rating'

urlpatterns = [
    path('', views.feedback, name='feedback'),
    # Add more URLs as needed
]
