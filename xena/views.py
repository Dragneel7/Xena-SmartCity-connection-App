from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from scoring import *
from django.db.models import Q

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
			r = UserProfile(userprofile = q,firstname = form.cleaned_data['firstname'],lastname = form.cleaned_data['lastname'],mobile = form.cleaned_data['mobile'],address = form.cleaned_data['address'],family_member = form.cleaned_data['family_member'], family_children = form.cleaned_data['family_children'])	
			r.save()	
			return redirect('xena:infofill')
	else:
		return render(request,'xena/home.html',{'form':form})


def info_fill(request):
	q = User.objects.get(username = request.user.username)
	r = UserProfile.objects.get(userprofile = q)
	view_form = ViewForm()
	comment_form = CommentForm()
	view = View.objects.all()

	print view
	context ={'user':r,'views':view,'view_form':view_form,'comment_form':comment_form}
	
	return render(request,'xena/user.html',context)
	

def comment_save(request):
	form = CommentForm()
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			commentobj = Comment.objects.create(
				usercomment = request.user,
				comment_view = form.cleaned_data['comment_view'],
				comment = form.cleaned_data['comment']
			)
		return HttpResponseRedirect(reverse('xena:infofill'))

def view_save(request):
	form = ViewForm()
	if request.method == "POST":
		form = ViewForm(data=request.POST)
		if form.is_valid():
			print "check" + form.cleaned_data['view']
			viewobj = View.objects.create(
					userview = request.user,
					view = form.cleaned_data['view']
				)	
		return HttpResponseRedirect(reverse('xena:infofill'))	

def query(request):
	organisation =Organisation.objects.all()
	print organisation
	return render(request,'xena/query.html',{'organisation':organisation})

def points(request):
	return render(request,'xena/points.html',{'user':request.user})	

from django.template.loader import render_to_string

def org(request):
	org = request.GET.get('org')
	print request.method
	print org
	org_object = Organisation.objects.get(org_name=org)
	return render(request,'xena/org_template.html',{'org':org_object})
	
def query_check(request):
	form = Org_queryForm()
	print request.method
	if request.method == "POST":
		
		form = Org_queryForm(request.POST)
		print form.is_valid()
		if form.is_valid():
			query = form.data['query_field']
			item = Organisation.objects.filter(Q(org_name__icontains=query))
			if item:
				#means the user knows the place take the user to the desired
				return render(request,'xena/org_template.html',{'org':item[0]})
			if not item:
				item = Organisation.objects.filter(tags__name__in=[query])
				if item:
					#code to save the query goes here
					#and return to the query page
					query_object = Org_query.objects.create(org_name=item[0],org_query=query)
					print "what"
					return HttpResponse(item)
			if not item:
				#search for desc goes here if found return	
				
				return HttpResponse(item)
			print query
			
