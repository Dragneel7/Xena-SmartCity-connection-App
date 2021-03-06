from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager

class UserProfile(models.Model):
	userprofile = models.OneToOneField(User)
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length =100)
	mobile = models.IntegerField()
	address = models.CharField(max_length = 300)
	family_member = models.IntegerField()
	family_children = models.IntegerField()
	def __unicode__(self):
		return self.firstname
	
class View(models.Model):
	userview = models.ForeignKey(User,related_name = 'views') 
	view = models.CharField(max_length = 200)
	comments = models.ManyToManyField(User,through='Comment')
	def __unicode__(self):
		return self.view

class Comment(models.Model):
	usercomment = models.ForeignKey(User)
	comment_view = models.ForeignKey(View)
	comment = models.CharField(max_length = 200)
	
	def __unicode__(self):
		return self.comment

class Organisation(models.Model):
	org_name = models.CharField(max_length=100)
	tags = TaggableManager() 
	org_desc = models.CharField(max_length=500)
	def __unicode__(self):
		return self.org_name


	

class Org_query(models.Model):
	org_name = models.ForeignKey(Organisation)
	org_query = models.CharField(max_length=200)

"""
class Vote(models.Model):
	uservote = models.ForeignKey(User)
	vote_view = models.OneToOneField(View)
	comment = models.BooleanField(default = False)

"""



# Create your models here.
