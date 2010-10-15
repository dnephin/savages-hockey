from django import forms
from hockey_register.register.models import Attendance


class AttendanceForm(forms.Form):
	state = forms.ChoiceField(choices=Attendance.STATE, initial='unknown')

