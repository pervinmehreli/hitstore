from django.shortcuts import render

# Create your views here.

def shopping_cart(request):
    return render(request, 'shopping-cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def wishlist(request):
    return render(request, 'wishlist.html')