from django.db import models

# Create your models here.
from django.utils import timezone

from hr_employees.models import EmployeeModel
from hr_tags.models import ResumeTagModel

class ResumeModel(models.Model):
	name = models.CharField(max_length=20, verbose_name='Name')
	sequence = models.IntegerField(verbose_name='Sequence')
	appointment_date = models.DateField(verbose_name='Appointment Date', default=timezone.now)
	note = models.TextField(max_length=100, verbose_name='Note')
	status = models.CharField(max_length=10, verbose_name='Status', default='draft')
	is_active = models.BooleanField(verbose_name='Is Active', default=False)
	create_date = models.DateField(verbose_name='Create Date', default=timezone.now)
	attachment = models.ImageField(verbose_name='Attachment', default=None, blank=True)
	employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE, default=None)
	tags = models.ManyToManyField(ResumeTagModel)

	def __str__(self):
		return self.name