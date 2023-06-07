from django.urls import path
from . import views

app_name = 'admin_module'

urlpatterns = [
    path('', views.admin_panel, name='admin_panel'),
    # Add more URLs as needed
]
