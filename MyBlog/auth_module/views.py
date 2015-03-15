from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
	if request.user.is_authenticated():
		return HttpResponse("You're already logged in!") 	
	return render(request, 'auth_module/login.html')

def login_action(request):
	username = request.POST['login']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponse("You was successfuly logged in!") 
	else:
		return HttpResponse("Fail of login!")


def registration(request):
	return render(request, 'auth_module/registration.html')

def log_out_action(request):
	logout(request)
	return render(request, 'auth_module/login.html')