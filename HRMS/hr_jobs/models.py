from django.db import models

# Create your models here.
from django.utils import timezone
from hr_departments.models import DepartmentModel
from hr_tags.models import JobTagModel

class JobModel(models.Model):
	name = models.CharField(max_length=20, verbose_name='Name')
	sequence = models.IntegerField(verbose_name='Sequence')
	open_date = models.DateField(verbose_name='Open Date', default=timezone.now)
	expected_salary = models.CharField(max_length=20, verbose_name='Expected Salary', default=None)
	note = models.TextField(max_length=100, verbose_name='Note')
	status = models.CharField(max_length=10, verbose_name='Status', default='draft')
	is_active = models.BooleanField(verbose_name='Is Active', default=False)
	create_date = models.DateField(verbose_name='Create Date', default=timezone.now)
	attachment = models.ImageField(verbose_name='Image', default=None, blank=True)
	department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE, default=None)
	tags = models.ManyToManyField(JobTagModel)

	def __str__(self):
		return self.name