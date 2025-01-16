from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'gainz_center_app/home.html')

def faqs(request):
    return render(request, 'gainz_center_app/faq.html')

def about(request):
    return render(request, 'gainz_center_app/about.html')

def our_gym(request):
    return render(request, 'gainz_center_app/our-gym.html')