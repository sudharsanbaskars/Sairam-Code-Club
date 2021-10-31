from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Event, Gallery

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class CreateEventForm(ModelForm):
	class Meta:
		model = Event
		fields = "__all__"

class CreateGalleryForm(ModelForm):
	class Meta:
		model = Gallery
		fields = "__all__"


