from django import forms
from django.forms import widgets
from hr_employees.models import EmployeeModel
from hr_tags.models import ContractTagModel

STATUS_CHOICES =(
	('draft', 'Draft'),
	('Open', 'Open'),
	('Confirm', 'Confirm')
)

class ContractForm(forms.Form):
	name = forms.CharField(max_length=20, label='Enter Name', widget=widgets.TextInput(attrs={'placeholder':'Your Name', 'class': 'form-control'}))
	rank = forms.DecimalField(label='Enter Rank', widget=widgets.NumberInput(attrs={'placeholder':'Your Rank' , 'class': 'form-control'}))
	start_date = forms.DateField(label='Enter Start Date', widget=widgets.DateInput(attrs={'type':'date' , 'class': 'form-control'}))
	end_date = forms.DateField(label='Enter End Date', widget=widgets.DateInput(attrs={'type':'date' , 'class': 'form-control'}))
	note = forms.CharField(max_length=100, label='Enter Note', widget=widgets.TextInput(attrs={'placeholder':'Your Note' , 'class': 'form-control'}))
	status = forms.ChoiceField(label='Status', choices=STATUS_CHOICES, widget=widgets.Select(attrs={'class': 'form-control'}))
	is_active = forms.BooleanField(label='Is Active', required=False)
	create_date = forms.DateField(label='Enter Create Date', widget=widgets.DateInput(attrs={'type':'date' , 'class': 'form-control'}))
	attachment = forms.ImageField(label='Upload Attachment', required=False, widget=widgets.ClearableFileInput(attrs={'class': 'form-control'}))
	employee = forms.ModelChoiceField(queryset=EmployeeModel.objects.all(), widget=widgets.Select(attrs={'class': 'form-control'}))
	tags = forms.ModelMultipleChoiceField(queryset=ContractTagModel.objects.all(), widget=widgets.CheckboxSelectMultiple())