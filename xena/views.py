from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

def log_in(request):
	form = AuthenticationForm()
	if request.method == "POST":
		form  = AuthenticationForm(data = request.POST)
		if form.is_valid():
			username = form.get_user()
			login(request,username)
			print type(username)
			return redirect('xena:home')
	else:
		return render(request,'xena/login.html',{'form':form})

def sign_up(request):
	
	form = UserCreationForm()
	if request.method == "POST":
		form = UserCreationForm(data = request.POST)
		if form.is_valid():
			
			form.save()
			user = User.objects.get(username = form.cleaned_data.get('username'))
			print type(user)
			user.backend='django.contrib.auth.backends.ModelBackend'
			login(request,user)
			return redirect('xena:home')
		else:
			print form.errors
	else:
		return render(request,'xena/signup.html',{'form':form})

def home(request):
	print request.user.username
	username = request.user.username
	return render(request,'xena/home.html',{'username':username})


# Create your views here.
