from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
<<<<<<< HEAD


# Create your forms here.
=======
from django.forms import ModelForm

	
	class Meta:
		model = 
		fields = ("",)


>>>>>>> f726452b778ad5e6e15ee4fe5a4249665ad5befb

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
<<<<<<< HEAD
		return user
=======
		return user

class UploadEvent(ModlelFrom):
	
>>>>>>> f726452b778ad5e6e15ee4fe5a4249665ad5befb
