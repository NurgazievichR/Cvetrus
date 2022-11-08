from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from apps.settings.models import Setting
from apps.user.forms import UserForm, LoginForm
from apps.user.models import User

def buyer_registration(request):
    settings = Setting.objects.latest('id')
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=form.cleaned_data['username'])
            user.set_password(form.cleaned_data['password'])
            user.status = '2'
            user.save()
            return redirect('mainpage')
    context = {
        'settings':settings,
        'form':form
    }   
    return render(request, 'user/buyer-reg.html', context)

def user_login(request):
    settings = Setting.objects.latest('id')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('mainpage')
            except Exception as _ex:
                print(_ex)
                messages.error(request, 'Не правильный логин, либо пароль')
    context = {
        'settings': settings,
        'form': form
    }
    return render(request, 'user/login.html', context)


def check(request):
    return render(request, 'message.html', {'settings':Setting.objects.latest('id')})