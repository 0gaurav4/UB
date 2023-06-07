from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Add this line
    # Other URL patterns for authentication app
]
