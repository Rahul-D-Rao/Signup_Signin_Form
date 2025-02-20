from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm
from .models import Profile

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            # Create the user
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            # Create the associated profile
            Profile.objects.create(
                user=user,
                profile_picture=form.cleaned_data.get('profile_picture'),
                address_line1=form.cleaned_data['address_line1'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                pincode=form.cleaned_data['pincode'],
                user_type=form.cleaned_data['user_type']
            )
            messages.success(request, "Signup successful. Please log in.")
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                profile = user.profile
                if profile.user_type == 'doctor':
                    return redirect('doctor_dashboard')
                else:
                    return redirect('patient_dashboard')
            except Profile.DoesNotExist:
                messages.error(request, "Profile not found.")
                return redirect('login')
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, 'accounts/login.html')

def doctor_dashboard(request):
    profile = request.user.profile
    return render(request, 'accounts/doctor_dashboard.html', {'profile': profile})

def patient_dashboard(request):
    profile = request.user.profile
    return render(request, 'accounts/patient_dashboard.html', {'profile': profile})

def user_logout(request):
    logout(request)
    return redirect('login')
