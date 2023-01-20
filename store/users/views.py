from django.shortcuts import redirect, render
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth


def login(request):
    if request.user.is_authenticated:
        return redirect('products:products')
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('products:products')
    else:
        form = UserLoginForm()
    context = {
        'form': form,
        'title': 'Вход',
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.user.is_authenticated:
        return redirect('products:products')
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
        'title': 'Регистрация',
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = UserProfileForm(instance=request.user)
    context = {'title': 'Профиль', 'form': form}
    return render(request, 'users/profile.html', context)
