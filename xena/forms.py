from .models import *
from django import forms

class UserProfileForm(forms.ModelForm):

	class Meta:
		model  = UserProfile
		fields = ('mobile','address','family_member','family_children')	
