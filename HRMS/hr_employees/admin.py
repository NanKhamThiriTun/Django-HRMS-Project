from django.contrib import admin

# Register your models here.
from hr_employees.models import EmployeeModel
admin.site.register(EmployeeModel)