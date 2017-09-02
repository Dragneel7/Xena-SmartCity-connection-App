from .models import *
from django import forms

class UserProfileForm(forms.ModelForm):

	class Meta:
		model  = UserProfile
		fields = ('firstname','lastname','mobile','address','family_member','family_children')

class ViewForm(forms.ModelForm):
	 
	class Meta:
		model = View
		fields = ('view',)


class CommentForm(forms.ModelForm):
	
	class Meta:
		model = Comment
		fields = ('comment','comment_view')			
