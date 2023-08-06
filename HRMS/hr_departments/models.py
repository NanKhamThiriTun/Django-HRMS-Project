from django.db import models
from django.utils import timezone

# Create your models here.
class DepartmentModel(models.Model):
	name = models.CharField(max_length=20, verbose_name='Name')
	sequence = models.IntegerField(verbose_name='Sequence')
	meeting_date = models.DateField(verbose_name='Meeting Date', default=timezone.now)
	total_employees = models.CharField(max_length=20, verbose_name='Total Employees', default=None)
	note = models.TextField(max_length=100, verbose_name='Note')
	status = models.CharField(max_length=10, verbose_name='Status', default='draft')
	is_active = models.BooleanField(verbose_name='Is Active', default=False)
	create_date = models.DateField(verbose_name='Create Date', default=timezone.now)
	attachment = models.ImageField(verbose_name='Attachment', default=None, blank=True)

	def __str__(self):
		return self.name