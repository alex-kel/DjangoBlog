from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def login_action(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("You was successfuly logged in!")
        else:
            return HttpResponse("Fail of login!")

    if request.method == 'GET':
        if request.user.is_authenticated():
            return HttpResponse("You're already logged in!")
        return render(request, 'auth_module/login.html')


def registration(request):
    if request.method == 'GET':
        return render(request, 'auth_module/registration.html')
    if request.method == 'POST':
        username = request.POST['login']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']
        if password == c_password:
            try:
                user = User.objects.create_user(username, email, password);
                user.save()
                return render(request, 'auth_module/login.html')
            except ValueError as e:
                return render(request, 'auth_module/registration.html', {'error' : e.__str__()})
        else:
            return render(request, 'auth_module/registration.html', {'error' : 'Passwords doesn`t match!'})

def log_out_action(request):
    logout(request)
    return render(request, 'auth_module/login.html')