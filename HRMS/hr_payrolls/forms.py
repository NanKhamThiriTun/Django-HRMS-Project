from django import forms
from hr_payrolls import models
from django.forms import widgets

STATUS_CHOICES =(
	('draft', 'Draft'),
	('open', 'Open'),
	('confirm', 'Confirm')
)

class PayrollForm(forms.ModelForm):

	class Meta:
		model = models.PayrollModel
		fields = "__all__"
		labels = {
			'name':'Enter Name',
			'salary':'Enter Salary',
			'ot_rate':'Enter OT Rate',
			'allowance':'Enter Allowance',
			'overtime':'Enter Overtime',
			'deduction':'Enter Deduction',
			'is_active':'Is Active',
			'attachment':'Upload Attachment'
		}

		widgets = {
			'name': widgets.TextInput(attrs={'placeholder':'Name', 'class': 'form-control'}),
			'salary': widgets.TextInput(attrs={'placeholder':'Salary', 'class': 'form-control'}),
			'ot_rate': widgets.TextInput(attrs={'placeholder':'OT Rate', 'class': 'form-control'}),
			'allowance': widgets.TextInput(attrs={'placeholder':'Allowance','class': 'form-control'}),
			'overtime': widgets.TextInput(attrs={'placeholder':'Overtime', 'class': 'form-control'}),
			'deduction': widgets.TextInput(attrs={'placeholder':'Deduction', 'class': 'form-control'}),
			'is_active': widgets.CheckboxInput(),
			'attachment': widgets.ClearableFileInput()
		}