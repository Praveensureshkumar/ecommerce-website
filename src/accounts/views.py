from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from accounts.models import *
from django.contrib.auth.decorators import login_required

# Render and process the login form to authenticate users
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

# Log the current user out and redirect to the store
def logout_view(request):
    logout(request)
    return redirect('ecommerce')

# Handle new user registration and create an associated CustomUser
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

@login_required
# Allow authenticated users to update their User and CustomUser profile
def profile_update_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = CustomUserUpdateForm(request.POST, request.FILES, instance=request.user.customuser)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = CustomUserUpdateForm(instance=request.user.customuser)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': request.user.customuser,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
# Delete the authenticated user's account when requested via POST
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Your account has been deleted.')
        return redirect('ecommerce')  # Change 'home' to your home or login page
    return redirect('profile')  # If GET request, do nothing


