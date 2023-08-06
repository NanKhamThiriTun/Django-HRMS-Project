from django.db import models

from django.utils import timezone


class AttendanceModel(models.Model):
	class Meta:
		permissions = (
			("view_contractmodel", "Can view contract model"),
		)
	name = models.CharField(max_length=20, verbose_name='Name')
	sign_in = models.DateTimeField(verbose_name='Sign In', default=None)
	sign_out = models.DateTimeField(verbose_name='Sign In', default=None)
	employee = models.CharField(max_length=20, verbose_name='Employe', default=None)
	is_active = models.BooleanField(verbose_name='Is Active', default=False)


	def __str__(self):
		return self.name