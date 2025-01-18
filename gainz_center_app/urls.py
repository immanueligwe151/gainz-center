from django.urls import path
from .views import home, faqs, about, our_gym, login, signup, logout, my_profile

urlpatterns = [
    path('', home, name='home'),
    path('faqs', faqs, name='faqs'),
    path('about', about, name='about'),
    path('our-gym', our_gym, name='our-gym'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('logout', logout, name='logout'),
    path('my-profile', my_profile, name='my-profile')

]