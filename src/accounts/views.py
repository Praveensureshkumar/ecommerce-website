from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from accounts.models import *
from django.http import HttpResponse

def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('ecommerce')
            else:
                form.add_error(None, 'Invalid username or password')

    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ecommerce')

def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            custom_user = CustomUser(user=user, phone_number=form.cleaned_data['phone_number'])
            custom_user.save()

            return redirect('accounts:login_view')
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})