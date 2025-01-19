from django.urls import path
from .views import home, faqs, about, our_gym, login, signup, logout, my_profile, my_prs, my_sessions, personal_trainers, change_email, change_password, delete_account

urlpatterns = [
    path('', home, name='home'),
    path('faqs', faqs, name='faqs'),
    path('about', about, name='about'),
    path('our-gym', our_gym, name='our-gym'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('logout', logout, name='logout'),
    path('my-profile', my_profile, name='my-profile'),
    path('my-prs', my_prs, name='my-prs'),
    path('my-sessions', my_sessions, name='my-sessions'),
    path('personal-trainers', personal_trainers, name='personal-trainers'),
    path('change-email', change_email, name='change-email'),
    path('change-password', change_password, name='change-password'),
    path('delete-account', delete_account, name='delete-account')
    

]