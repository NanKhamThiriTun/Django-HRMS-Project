from django.db import models

# Create your models here.
from django.utils import timezone
from hr_jobs.models import JobModel
from hr_tags.models import ExpenseTagModel

class  ExpenseModel(models.Model):

	name = models.CharField(max_length=20, verbose_name='Name')
	quantity = models.IntegerField(verbose_name='Quantity',  default=None)
	product = models.CharField(max_length=20, verbose_name='Product',  default=None)
	price = models.CharField(max_length=20, verbose_name='Price',  default=None)
	total = models.CharField(max_length=20, verbose_name='Total',  default=None)
	reason = models.CharField(max_length=10, verbose_name='Status', default='draft')
	is_active = models.BooleanField(verbose_name='Is Active', default=False)
	attachment = models.ImageField(verbose_name='Image', default=None, blank=True)
	job = models.ForeignKey(JobModel, on_delete=models.CASCADE, default=None)
	tags = models.ManyToManyField(ExpenseTagModel)

