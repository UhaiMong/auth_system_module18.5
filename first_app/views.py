from django.shortcuts import render, redirect
from . forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created Successfully!')
            form.save(commit=True)
            return redirect('homepage')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login Function


def userLogin(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userPassword = form.cleaned_data['password']
            user = authenticate(username=name, password=userPassword)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged In Successfully')
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user})
    else:
        return redirect('login')

# Logout function


def userLogout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('homepage')

# Change Password with using Old Password


def changPassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'changePass.html', {'form': form})
# Change Password without using Old Password


def resetPassword(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'changePass.html', {'form': form})
