from django.shortcuts import render, redirect
from .models import FAQs, Equipment, Users
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your views here.
def home(request):
    manually_clear_messages(request)
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
    manually_clear_messages(request)

    if 'username' in request.session:
        return redirect('my-profile') #redirects logged in user to profile page if they try to cheekily type in the url for the login page

    if request.method == 'POST':
        username = request.POST.get('username-sign-in')
        password = request.POST.get('password-sign-in')

        try:
            user = Users.objects.get(username=username)
            if user.check_password(password):
                request.session['username'] = username  # Store session
                return redirect('my-profile')  #to redirect to the profile page
            else:
                messages.error(request, "Your username or password is incorrect, please try again.", extra_tags="login_failure")
        except Users.DoesNotExist:
            messages.error(request, "This user doesn't exist, please check and try again", extra_tags="login_failure")

        return render(request, 'gainz_center_app/login.html', { 'username': username })
    return render(request, 'gainz_center_app/login.html')

def signup(request):
    if 'username' in request.session:
        return redirect('my-profile')

    if request.method == 'POST':
        valid = True
        name = request.POST.get('name-sign-up', '').strip()
        username = request.POST.get('username-sign-up', '').strip()
        email = request.POST.get('email-sign-up', '').strip()
        mobile = request.POST.get('number-sign-up', '').strip()
        dob = request.POST.get('dob-sign-up', '').strip()
        password1 = request.POST.get('password1', '').strip()
        password2 = request.POST.get('password2', '').strip()

        if password1 != password2:
            messages.error(request, "Sorry, your passwords don't match, please check and try again.", extra_tags="password")
            valid = False

        if Users.objects.filter(username=username).exists():
            messages.error(request, "Sorry, this username has already been taken, please try another one.", extra_tags="username")
            valid = False

        if Users.objects.filter(email=email).exists():
            messages.error(request, "Sorry, this email has already been registered. Please try another one.", extra_tags="email")
            valid = False
        
        if Users.objects.filter(mobile=mobile).exists():
            messages.error(request, "Sorry, this mobile has already been registered. Please try another one.", extra_tags="mobile")
            valid = False
        
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Sorry, you've entered an invalid email, please try again.", extra_tags="email")
            valid = False

        if valid:
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
        else:
            return render(request, 'gainz_center_app/signup.html', {
            'name': name,
            'username': username,
            'email': email,
            'mobile': mobile,
            'dob': dob,
        })
    return render(request, 'gainz_center_app/signup.html')

def logout(request):
    request.session.flush()
    messages.success(request, "Logged out successfully.")
    manually_clear_messages(request)
    return redirect('home')

def my_profile(request):
    user = None #declaring it at the head here so it's within scope
    if 'username' not in request.session:
        return redirect('home') #go back to home page if user is not logged in
    else:
        username = request.session['username'] #retrieves username from session
        try:
            user = Users.objects.get(username=username)
        except Users.DoesNotExist:
            return redirect('login') #should not be needed since user can't access the page anyway if not logged in

    return render(request, 'gainz_center_app/my-profile.html', { 'user': user })

def my_sessions(request):
    if 'username' not in request.session:
        return redirect('home')

    return render(request, 'gainz_center_app/my-sessions.html')

def my_prs(request):
    if 'username' not in request.session:
        return redirect('home')

    return render(request, 'gainz_center_app/my-prs.html')

def personal_trainers(request):
    if 'username' not in request.session:
        return redirect('home')

    return render(request, 'gainz_center_app/personal-trainers.html') 




def manually_clear_messages(request):
    if '_messages' in request.session:
        del request.session['_messages']