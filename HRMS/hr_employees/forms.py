from django import forms
from hr_employees import models
from django.forms import widgets

STATUS_CHOICES =(
	('draft', 'Draft'),
	('open', 'Open'),
	('confirm', 'Confirm')
)

class EmployeeForm(forms.ModelForm):

	class Meta:
		model = models.EmployeeModel
		fields = "__all__"
		labels = {
			'name':'Enter Name',
			'age':'Enter Age',
			'birthday':'Enter Birthday',
			'address':'Enter Address',
			'email':'Enter Email',
			'is_married':'Enter Is Married',
			'gender':'Enter Gender',
			'joining_date':'Enter Joining Date',
			'attachment':'Upload Attachment'
		}

		widgets = {
			'name': widgets.TextInput(attrs={'placeholder':'Name', 'class': 'form-control'}),
			'age': widgets.NumberInput(attrs={'placeholder':'Age', 'class': 'form-control'}),
			'birthday': widgets.DateInput(attrs={'placeholder':'Birthday','type': 'date', 'class': 'form-control'}),
			'address': widgets.TextInput(attrs={'placeholder':'Address', 'class': 'form-control'}),
			'email': widgets.TextInput(attrs={'placeholder':'Email', 'class': 'form-control'}),
			'is_married': widgets.CheckboxInput(attrs={'class': 'form-check-input'}),
			'gender': widgets.Select(choices=STATUS_CHOICES, attrs={'class': 'form-control'}),
			'joining_date': widgets.DateInput(attrs={'placeholder':'Joining Date', 'type': 'date', 'class': 'form-control'}),
			'attachment': widgets.ClearableFileInput()
		}

	