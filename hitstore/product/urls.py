from django.urls import path

from . import views

urlpatterns = [
    path('product/', views.product, name='product'),
    path('single-product/', views.single_product, name='single-product')
]