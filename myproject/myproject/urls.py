"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('account/', include('account.urls')),
    path('admin_module/', include('admin_module.urls')),
    path('course/', include('course.urls')),
    path('profiles/', include('profiles.urls')),
    path('search/', include('search.urls')),
    path('authentication/', include('authentication.urls')),
    path('study_material/', include('study_material.urls')),
    path('cart/', include('cart.urls')),
    path('order_management/', include('order_management.urls')),
    path('payment_gateway/', include('payment_gateway.urls')),
    path('career_counseling/', include('career_counseling.urls')),
    path('video_lectures/', include('video_lectures.urls')),
    path('notification/', include('notification.urls')),
    path('feedback_rating/', include('feedback_rating.urls')),
    
     path('', include('dashboard.urls')), 
]
