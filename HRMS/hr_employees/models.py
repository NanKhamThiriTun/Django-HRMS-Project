from django.db import models

# Create your models here.
from django.utils import timezone

class EmployeeModel(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    age = models.IntegerField(verbose_name='Age')
    birthday = models.DateField(verbose_name='Birthday', default=timezone.now)
    address = models.TextField(max_length=100, verbose_name='Address')
    email = models.EmailField(max_length=50, default='test@gmail.com')
    gender = models.CharField(max_length=10, verbose_name='Gender', default='other')
    is_married = models.BooleanField(verbose_name='Is Married', default=False)
    joining_date = models.DateTimeField(verbose_name='Joining Date', default=timezone.now)
    image = models.ImageField(verbose_name='Image', default=None)