from profile import Profile

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

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


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    messages.info(request, "User was logged out")
    return redirect('home_page')


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
            context = {'form': form}
            # messages.error(request, "An error has occurred during registration")
            return render(request, 'user/register.html', context)

    return render(request, 'user/register.html', context)


@login_required(login_url='login')
def profile(request):
    _profile = request.user.profile
    questions = _profile.question_set.count()
    reply = _profile.reply_set.count()
    votesQuestions = _profile.votequestion_set.count()
    votesReply = _profile.votereply_set.count()
    finalVotes = votesQuestions + votesReply
    context = {'questions': questions, 'reply': reply, 'votes': finalVotes}
    return render(request, 'user/dashboard.html', context)


@login_required(login_url='login')
def profileManage(request):
    profile = request.user.profile
    questions = profile.question_set.all().order_by('-date_created')
    context = {'questions': questions}
    return render(request, 'user/dashboard_manage.html', context)
