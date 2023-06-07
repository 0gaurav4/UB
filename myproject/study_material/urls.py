from django.urls import path
from . import views

app_name = 'study_material'

urlpatterns = [
    path('', views.study_material, name='study_material'),
    # Add more URLs as needed
]
