from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.views.generic.edit import CreateView
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def register(request):
    return render(request, 'users/register.html')


def profile(request):
    return render(request, "users/user-profile.html")


def landing(request):
    return render(request, 'users/landing.html')


def login(request):
    form = UserLoginForm()

    if request.user.username:
        return HttpResponseRedirect("/users/profile")

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user and user.is_staff and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/questionaries/questionary-list/")
        elif user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/users/profile")

    return render(request, "users/login.html", {'form': form})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/landing")


def main_page(request):
    return redirect('landing/')
