from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


# Create your views here.


def login_user(request, next_url='vacancies'):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next_url)
        else:
            print("username or password is incorrect")

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('vacancies')