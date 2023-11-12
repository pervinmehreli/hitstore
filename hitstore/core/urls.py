from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about-us/', views.about_us, name='about'),
    path('contact-us/', views.contact_us, name='contact'),
    path('faq/', views.faq, name='faq'),
]