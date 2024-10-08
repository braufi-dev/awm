from django.shortcuts import render, redirect
from .models import WorldBorder, Profile as user

# authentication
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm

from django.contrib.gis.geos.point import Point
from django.http import JsonResponse

# Create your views here.

# View that reads the locations from world borders and passes on to maps
def map_view(request):
    # expand the code by setting the authentication here
    if request.user.is_authenticated:
        user_profile = user.objects.get(user=request.user)
        location = user_profile.location
        return render(request, 'map.html', {'user': request.user, 'location': location})
    else:
        return render(request, 'login.html')
    

#login & logout views
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

#Signup view
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')  # Redirect to the home page after successful signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def update_location(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        user = request.profile
        user.location = Point(float(longitude), float(latitude))
        user.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
