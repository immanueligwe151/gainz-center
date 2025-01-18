from django.shortcuts import render, redirect
from .models import FAQs, Equipment, Users
from django.contrib import messages

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

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username-sign-in')
        password = request.POST.get('password-sign-in')

        try:
            user = Users.objects.get(username=username)
            if user.check_password(password):
                request.session['username'] = username  # Store session
                messages.success(request, "Login successful.")
                return redirect('home')  #to change to redirect to the profile page
            else:
                messages.error(request, "Invalid credentials.")
        except Users.DoesNotExist:
            messages.error(request, "User does not exist.")

        return redirect('login')
    return render(request, 'gainz_center_app/login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name-sign-up')
        username = request.POST.get('username-sign-up')
        email = request.POST.get('email-sign-up')
        mobile = request.POST.get('number-sign-up')
        dob = request.POST.get('dob-sign-up')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Sorry, your passwords don't match, please check and try again.")
            return redirect('signup')

        if Users.objects.filter(username=username).exists():
            messages.error(request, "Sorry, this username has already been taken, please try another one.")
            return redirect('signup')

        if Users.objects.filter(email=email).exists():
            messages.error(request, "Sorry, this email has already been registered. Please try another one.")
            return redirect('signup')
        
        if Users.objects.filter(mobile=mobile).exists():
            messages.error(request, "Sorry, this mobile has already been registered. Please try another one.")
            return redirect('signup')

        user = Users(
            username=username,
            person_name=name,
            email=email,
            mobile=mobile,
            dob=dob,
        )
        user.set_password(password1)  #this hashes the password and saves it to the model
        user.save()

        request.session['username'] = username
        messages.success(request, f"Welcome, {name}! You have been successfully signed up and are now logged in.")
        return redirect('my-profile')
    return render(request, 'gainz_center_app/signup.html')

def logout(request):
    request.session.flush()
    messages.success(request, "Logged out successfully.")
    return redirect('home')

def my_profile(request):
    return render(request, 'gainz_center_app/my-profile.html')

    