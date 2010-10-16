from django import forms
from django.forms import ModelForm
from hockey_register.register.models import Attendance
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class AttendanceForm(forms.Form):
	state = forms.ChoiceField(choices=Attendance.STATE, initial='unknown')


class RegisterForm(UserCreationForm):

	class Meta:
		model = User
		fields = ("username",'email', 'first_name', 'last_name')

	email = forms.EmailField()
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)

