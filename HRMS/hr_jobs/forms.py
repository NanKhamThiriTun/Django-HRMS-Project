from django import forms
from hr_jobs import models
from django.forms import widgets

STATUS_CHOICES =(
	('draft', 'Draft'),
	('open', 'Open'),
	('confirm', 'Confirm')
)

class JobForm(forms.ModelForm):

	class Meta:
		model = models.JobModel
		fields = "__all__"
		labels = {
			'name':'Enter Name',
			'sequence':'Enter Sequence',
			'open_date':'Enter Open Date',
			'expected_salary':'Enter Expected Salary',
			'note':'Enter Note',
			'status':'Enter Status',
			'is_active':'Is Active',
			'create_date':'Enter Crate Date',
			'attachment':'Upload Attachment'
		}

		widgets = {
			'name': widgets.TextInput(attrs={'placeholder':'Name', 'class': 'form-control'}),
			'sequence': widgets.NumberInput(attrs={'placeholder':'Sequence', 'class': 'form-control'}),
			'expected_salary': widgets.TextInput(attrs={'placeholder':'Expected Salary', 'class': 'form-control'}),
			'open_date': widgets.DateInput(attrs={'placeholder':'Open Date', 'type': 'date', 'class': 'form-control'}),
			'note': widgets.TextInput(attrs={'placeholder':'Note', 'class': 'form-control'}),
			'status': widgets.Select(choices=STATUS_CHOICES, attrs={'class': 'form-control'}),
			'is_active': widgets.CheckboxInput(),
			'create_date': widgets.DateInput(attrs={'placeholder':'Create Date', 'type': 'date', 'class': 'form-control'}),
			'attachment': widgets.ClearableFileInput()
		}