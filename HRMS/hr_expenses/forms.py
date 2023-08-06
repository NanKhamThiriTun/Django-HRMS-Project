from django import forms
from hr_expenses import models
from django.forms import widgets

STATUS_CHOICES =(
	('draft', 'Draft'),
	('open', 'Open'),
	('confirm', 'Confirm')
)

class ExpenseForm(forms.ModelForm):

	class Meta:
		model = models.ExpenseModel
		fields = "__all__"
		labels = {
			'name':'Enter Name',
			'quantity':'Enter Quantity',
			'product':'Enter Product',
			'price':'Enter Price',
			'total':'Enter Total',
			'reason':'Enter reason',
			'is_active':'Is Active',
			'attachment':'Upload Attachment',
			'job': 'Job',
		}

		widgets = {
			'name': widgets.TextInput(attrs={'placeholder':'Name', 'class': 'form-control'}),
			'quantity': widgets.NumberInput(attrs={'placeholder':'Quantity', 'class': 'form-control'}),
			'product': widgets.TextInput(attrs={'placeholder':'Product', 'class': 'form-control'}),
			'price': widgets.TextInput(attrs={'placeholder':'Price', 'class': 'form-control'}),
			'total': widgets.TextInput(attrs={'placeholder':'Total', 'class': 'form-control'}),
			'reason': widgets.TextInput(attrs={'placeholder':'reason', 'class': 'form-control'}),
			'is_active': widgets.CheckboxInput(),
			'attachment': widgets.ClearableFileInput(),
			'job': widgets.Select(attrs={'class': 'form-control'}),
			'tags': widgets.CheckboxSelectMultiple()

		}