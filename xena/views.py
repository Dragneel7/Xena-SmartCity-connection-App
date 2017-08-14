from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.decorators import login_required

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
			user.backend='django.contrib.auth.backends.ModelBackend'
			login(request,user)
			return redirect('xena:home')
		else:
			print form.errors
	else:
		return render(request,'xena/signup.html',{'form':form})

@login_required
def home(request):
	print request.user.username
	username = request.user.username
	form = UserProfileForm()
	return render(request,'xena/home.html',{'username':username,'form':form})

def info_save(request):
	print "hello"
	form = UserProfileForm()
	if request.method == "POST":
		form = UserProfileForm(data = request.POST)
		if form.is_valid():
			q = User.objects.get(username = request.user.username)
			q.save(commit = False)
			q.userprofile_set.create(mobile = form.cleaned_data('mobile'),address = form.cleaned_data('address'),family_member = form.cleaned_data('family_member'), family_children = form.cleaned_data('family_children'))
			return render(request,'xena/user.html')
	else:
		return render(request,'xena/home.html',{'form':form})
	

def log_out(request):
	logout(request)
	form = AuthenticationForm()
	return render(request,'xena/login.html',{'form':form})
