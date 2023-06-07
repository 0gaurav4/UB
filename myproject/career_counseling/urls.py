from django.urls import path
from . import views

app_name = 'career_counseling'

urlpatterns = [
    path('', views.career_counseling, name='career_counseling'),
    # Add more URLs as needed
]
