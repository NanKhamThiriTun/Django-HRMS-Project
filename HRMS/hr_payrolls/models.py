from django.db import models

# Create your models here.
from django.utils import timezone
from hr_departments.models import DepartmentModel
from hr_tags.models import PayrollTagModel



class PayrollModel(models.Model):
		
	name = models.CharField(max_length=20, verbose_name='Name')
	salary = models.CharField(max_length=20, verbose_name='Expected Salary', default=None)
	ot_rate = models.CharField(max_length=20, verbose_name='OT Rate', default=None)
	allowance = models.CharField(max_length=20, verbose_name='Allowance', default=None)
	overtime = models.CharField(max_length=20, verbose_name='Overtime', default=None)
	deduction = models.CharField(max_length=10, verbose_name='Deduction', default=None)
	is_active = models.BooleanField(verbose_name='Is Active', default=False)
	attachment = models.ImageField(verbose_name='Image', default=None, blank=True)
	department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE, default=None)
	tags = models.ManyToManyField(PayrollTagModel)

	def __str__(self):
		return self.name