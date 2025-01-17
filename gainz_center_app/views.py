from django.shortcuts import render
from .models import FAQs, Equipment

# Create your views here.
def home(request):
    return render(request, 'gainz_center_app/home.html')

def faqs(request):
    faqs = FAQs.objects.all()
    return render(request, 'gainz_center_app/faq.html', { 'faqs' : faqs })

def about(request):
    return render(request, 'gainz_center_app/about.html')

def our_gym(request):
    equipments = Equipment.objects.all()
    return render(request, 'gainz_center_app/our-gym.html', { 'equipments' : equipments })