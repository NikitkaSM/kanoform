from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages, auth
from config import settings


def register(request):
    form = UserRegisterForm()

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        email = request.POST.get('email')
        username = request.POST.get('username')

        if User.objects.get(email=email).exists():
            return messages.error(request, "Пользователь с такой почтой уже существует.")

        if User.objects.get(username=username).exists():
            return messages.error(request, "Пользователь с таким юзернеймом уже существует.")

        if form.is_valid():
            ins = form.save()
            email = form.cleaned_data['email']

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            ins.email = email
            ins.save()
            form.save_m2m()

            return HttpResponseRedirect('/landing')

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, "users/user_profile.html")


def landing(request):
    return render(request, 'users/landing.html')


def login(request):
    form = UserLoginForm()

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        else:
            return messages.error(request, 'Такой пользователь не существует')

    return render(request, "users/login.html", {'form': form})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/landing")


def main_page(request):
    return redirect('landing/')
