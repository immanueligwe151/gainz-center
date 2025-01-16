from django.urls import path
from .views import home, faqs, about, our_gym

urlpatterns = [
    path('', home, name='home'),
    path('faqs', faqs, name='faqs'),
    path('about', about, name='about'),
    path('our-gym', our_gym, name='our-gym'),
]