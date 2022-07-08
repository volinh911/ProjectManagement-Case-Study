from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import CustomUserCreationForm

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home_page')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exists")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.error(request, "Username or Password is incorrect")
    return render(request, 'user/login.html')


def logoutUser(request):
    logout(request)
    messages.error(request, "User was logged out")
    return redirect('login')

def registerUser(request):
    form = CustomUserCreationForm()
    context = {'form': form}

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User account was created")

            login(request, user)
            return redirect('home_page')

        else:
            messages.error(request, "An error has occurred during registration")

    return render(request, 'user/register.html', context)

def profile(request):
    return render(request, 'user/profile.html')
