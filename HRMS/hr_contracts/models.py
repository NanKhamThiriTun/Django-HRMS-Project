from django.db import models

# Create your models here.
from django.utils import timezone

from hr_employees.models import EmployeeModel
from hr_tags.models import ContractTagModel

class ContractModel(models.Model):

	name = models.CharField(max_length=20, verbose_name='Name')
	rank = models.IntegerField(verbose_name='Rank')
	start_date = models.DateField(verbose_name='Start Date', default=timezone.now)
	end_date = models.DateField(verbose_name='End Date', default=timezone.now)
	note = models.TextField(max_length=100, verbose_name='Note')
	status = models.CharField(max_length=10, verbose_name='Status', default='draft')
	is_active = models.BooleanField(verbose_name='Is Active', default=False)
	create_date = models.DateField(verbose_name='Create Date', default=timezone.now)
	attachment = models.ImageField(verbose_name='Image', default=None)
	employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE, default=None)
	tags = models.ManyToManyField(ContractTagModel)

	def __str__(self):
		return self.name