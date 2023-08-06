from django.contrib import admin

# Register your models here.
from hr_payrolls.models import PayrollModel
admin.site.register(PayrollModel)