from django.shortcuts import render
from .models import User

def profile(request):
    user = User.objects.get(id=request.user.id)
    return render(request, 'account/profile.html', {'user': user})

# Add more views as needed

