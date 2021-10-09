from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

def login_view(request):
    "A login endpoint to allow user login"
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(request.get_full_path_info())
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            context = {'error': 'incorrect username or password'}
            return render(request,template_name='accounts/login.html',context=context)

    context = {}
    return render(request, 'accounts/login.html',context=context)

def logout_view(request):
    "A logout endpoint to allow user logout"
    logout(request)
    context = {}
    return HttpResponseRedirect(reverse('login'))


def register_view(request):
    "A register endpoint to allow user register"
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if all([username, password]):
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponseRedirect(reverse('register'))
    context = {}
    return render(request, 'accounts/register.html',context=context)

