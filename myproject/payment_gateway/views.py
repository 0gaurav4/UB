from django.shortcuts import render

def payment(request):
    # Logic for payment gateway integration
    return render(request, 'payment_gateway/payment.html')
