from django.shortcuts import render, redirect
from .models import FAQs, Equipment, Users, MySessions, Exercises, ExerciseTypes, SessionExercises, PersonalTrainers
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from datetime import datetime
import json

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
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

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
    else:
        username = request.session['username']
        try:
            sessions = MySessions.objects.filter(username__username=username)
            exercises = SessionExercises.objects.filter(username__username=username)
            types = ExerciseTypes.objects.all()
            list_exercises = Exercises.objects.all()
            return render(request, 'gainz_center_app/my-sessions.html', { 'sessions': sessions, 'exercises': exercises, 'types': types, 'list_exercises': list_exercises })
        except Exception:
            return render(request, 'gainz_center_app/my-sessions.html', { 'sessions': [], 'exercises': [], 'types': [], 'list_exercises': [] })


def personal_trainers(request):
    if 'username' not in request.session:
        return redirect('home')

    pt_list = PersonalTrainers.objects.all()
    return render(request, 'gainz_center_app/personal-trainers.html', { 'pt_list': pt_list }) 


def change_email(request):
    if 'username' in request.session:
        username = request.session['username']
        try:
            user = Users.objects.get(username=username)
            email = request.POST.get('email-change', '').strip()
            user.email = email
            user.save()
            messages.success(request, 'You have succesfully changed your email.')
            return redirect('my-profile')
        except Users.DoesNotExist:
            messages.failure(request, 'There was an issue, please try again.')
            return redirect('my-profile')

def change_password(request):
    if 'username' in request.session:
        username = request.session['username']
        try:
            user = Users.objects.get(username=username)
            old_pass = request.POST.get('old-pass')
            new_pass = request.POST.get('new-pass')
            new_pass_conf = request.POST.get('new-pass-conf')

            if user.check_password(old_pass):
                if new_pass == new_pass_conf:
                    user.set_password(new_pass)
                    user.save()
                    messages.success(request, "Your password has been changed succesfully!")
                    return redirect('my-profile')
                else:
                    messages.error(request, "Your new passwords don't match. Please try again")
                    return redirect('my-profile')
            else:
                messages.error(request, "Your entered old password is incorrect, please try again.")
                return redirect('my-profile')
        except Users.DoesNotExist:
            return redirect('my-profile')

def delete_account(request):
    if 'username' in request.session:
        username = request.session['username']
        try:
            user = Users.objects.get(username=username)
            password = request.POST.get('pass-acc-del')

            if user.check_password(password):
                user.delete()
                messages.success(request, "You have succesfully deleted your account.")
                return logout(request)
            else:
                messages.error(request, "The password you entered was wrong. Please try again.")
                return redirect('my-profile')
        except Users.DoesNotExist:
            return redirect('my-profile')

def add_new_session(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # this is to extract and validate date and time fields
            date_str = data.get('date')
            start_time_str = data.get('startTime')
            end_time_str = data.get('endTime')
            exercises = data.get('exercises', [])

            start_time = datetime.fromisoformat(start_time_str)
            end_time = datetime.fromisoformat(end_time_str)
            date = datetime.fromisoformat(date_str)

            # creates the session object
            my_session = MySessions.objects.create(
                username=Users.objects.get(username=request.session['username']), 
                date_of_session=date, 
                pre_made=0, 
                check_in_time=start_time, 
                check_out_time=end_time
            )

            # creates the exercises
            for exercise_data in exercises:
                name = exercise_data['name']
                sets = exercise_data['set']
                reps = exercise_data['rep']
                weight = exercise_data['weight']
                unit = exercise_data['unit']

                # gets the exercise object
                exercise_obj = Exercises.objects.get(exercise_name=name)

                # saves the exercises linked to the session
                SessionExercises.objects.create(
                    username=Users.objects.get(username=request.session['username']),
                    session_id=my_session,
                    exercise_name=exercise_obj,
                    set_number=sets,
                    reps=reps,
                    weight=weight,
                    unit=unit
                )

            return JsonResponse({'message': 'Data received successfully!'}, status=201)

        except Exercises.DoesNotExist:
            return JsonResponse({'error': 'Invalid exercise name'}, status=400)
        except ValueError as e:
            return JsonResponse({'error': f'Invalid datetime format: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'message': 'Invalid request method.'}, status=405)

