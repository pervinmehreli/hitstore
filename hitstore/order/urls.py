from django.urls import path

from . import views

urlpatterns = [
    path('shopping-cart/', views.shopping_cart, name='shopping-cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('wishlist/', views.wishlist, name='wishlist')
]