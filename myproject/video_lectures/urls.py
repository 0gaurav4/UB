from django.urls import path
from . import views

app_name = 'video_lectures'

urlpatterns = [
    path('', views.video_lectures, name='video_lectures'),
    # Add more URLs as needed
]
