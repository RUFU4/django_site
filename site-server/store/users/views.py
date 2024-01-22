from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from users.forms import UserLoginForm, UserRegistraterForm, UserProfileForm
from django.contrib import auth
from django.urls import reverse


def login(request):
    error = ''
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
        error = 'Что-то пошло не так'

    data = {'form': form}

    return render(request, 'users/login.html', data)

def register(request):
    error =''
    if request.method == 'POST':
        form = UserRegistraterForm(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserRegistraterForm()
        error = 'Что-то пошло не так'
        print(form.errors)
    data = {'form': form}

    return render(request, 'users/register.html', data)

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'products/user.html', context)
