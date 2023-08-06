from django import forms
from hr_attendances import models
from django.forms import widgets

STATUS_CHOICES =(
	('draft', 'Draft'),
	('open', 'Open'),
	('confirm', 'Confirm')
)

class AttendanceForm(forms.ModelForm):

	class Meta:
		model = models.AttendanceModel
		fields = "__all__"
		labels = {
			'name':'Enter Name',
			'sign_in':'Sign In',  
            'sign_out':'Sign Out',
            'employee':'Employee',  
			'is_active':'Is Active'
		}

		widgets = {
			'name': widgets.TextInput(attrs={'placeholder':'Name', 'class': 'form-control'}),
			'sign_in': widgets.DateTimeInput(attrs={'type':'datetime-local','Sign In' 'class': 'form-control'}),
            'sign_out': widgets.DateTimeInput(attrs={'type':'datetime-local','Sign Out' 'class': 'form-control'}),
            'employee': widgets.TextInput(attrs={'placeholder':'Employee','class': 'form-control'}),
			'is_active': widgets.CheckboxInput()
		}