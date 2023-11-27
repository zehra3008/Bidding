from .models import ActiveList, UserBid, UserComment
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1','password2']

class CreateListForm(forms.ModelForm):
	class Meta:
		model = ActiveList
		fields = '__all__'

class UserBidForm(forms.ModelForm):
	class Meta:
		model = UserBid
		fields = ['userbid']
		labels = {
			'userbid' : 'Place Bid '
		}

class UserCommentForm(forms.ModelForm):
	class Meta:
		model = UserComment
		fields = ['comment']