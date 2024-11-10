from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .froms import LoginForm, RegistrationForm
from django.contrib import auth
from django.urls import reverse


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/tasks/')
    else:
        form = LoginForm()
    context = {'form': form,
               'msg': 'Авторизация',
               'title': 'Форма авторизации'}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = RegistrationForm()
    context = {'form': form,
               'msg': 'Регистрация',
               'title': 'Форма регистрации'}
    return render(request, 'users/registration.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/main/')
