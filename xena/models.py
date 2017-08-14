from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
	userprofile = models.OneToOneField(User)
	mobile = models.IntegerField()
	address = models.CharField(max_length = 300)
	family_member = models.IntegerField()
	family_children = models.IntegerField()

class View(models.Model):
	userview = models.ForeignKey(User,related_name = 'views') 
	view = models.CharField(max_length = 200)
	
	def __unicode__(self):
		return self.view

class Comment(models.Model):
	usercomment = models.ForeignKey(User)
	comment_view = models.ForeignKey(View)
	comment = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.comment

class Vote(models.Model):
	uservote = models.ForeignKey(User)
	vote_view = models.OneToOneField(View)
	comment = models.BooleanField(default = False)





# Create your models here.
