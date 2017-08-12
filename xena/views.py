from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout
from django.core.urlresolvers import reverse

def home(request):
	return render(request,'xena/login.html')

def log_in(request):
	form = AuthenticationForm()
	if request.method == "POST":
		form  = AuthenticationForm(data = request.POST)
		if form.is_valid():
			login(request,form.get_user())
			return redirect('home')
	else:
		return render(request,'xena/login.html',{'form':form})

def sign_up(request):
	print "hello"
	form = UserCreationForm()
	if request.method == "POST":
		form = UserCreationForm(data = request.POST)
		if form.is_valid():
			print "hello"
			form.save()
			
			return redirect('home',request)
		else:
			print form.errors
	else:
		return render(request,'xena/signup.html',{'form':form})

# Create your views here.
