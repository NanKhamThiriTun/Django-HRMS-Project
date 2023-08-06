from django.contrib import admin

# Register your models here.
from .models import JobTagModel
from .models import EmployeeTagModel
from .models import ContractTagModel
from .models import ResumeTagModel
from .models import ExpenseTagModel
from .models import PayrollTagModel
from .models import AttandanceTagModel


admin.site.register(ExpenseTagModel)
admin.site.register(JobTagModel)
admin.site.register(EmployeeTagModel)
admin.site.register(ContractTagModel)
admin.site.register(ResumeTagModel)
admin.site.register(PayrollTagModel)
admin.site.register(AttandanceTagModel)