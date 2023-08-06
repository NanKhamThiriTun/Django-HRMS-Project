from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import ListView, CreateView
from django.contrib.auth import get_user_model

from hr_employees.models  import EmployeeModel
from hr_departments.models import DepartmentModel
from hr_contracts.models import ContractModel
from hr_attendances.models import AttendanceModel
from hr_recruitments.models import ResumeModel
from hr_expenses.models import ExpenseModel
from hr_jobs.models import JobModel

from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm

class Dashboard(LoginRequiredMixin,ListView):
	login_url = reverse_lazy('login')
	template_name = 'dashboard.html'
	model = get_user_model()
	context_object_name = 'qset'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs) 
		context['emp_total'] = EmployeeModel.objects.all().count()
		context['atte_total'] = AttendanceModel.objects.all().count()
		context['dept_total'] = DepartmentModel.objects.all().count()
		context['cont_total'] = ContractModel.objects.all().count()
		context['rect_total'] = ResumeModel.objects.all().count()
		context['expen_total'] = ExpenseModel.objects.all().count()
		context['payr_total'] = ExpenseModel.objects.all().count()
		context['job_total'] = JobModel.objects.all().count()
		context['admin_count'] = get_user_model().objects.all().count()
		context['employees'] = EmployeeModel.objects.order_by('-id')
		context['departments'] = DepartmentModel.objects.order_by('-id')
		context['expenses'] = ExpenseModel.objects.order_by('-id')
		context['contracts'] = ContractModel.objects.order_by('-id')
		context['jobs'] = JobModel.objects.order_by('-id')
		context['attendances'] = AttendanceModel.objects.order_by('-id')
		context['recruitments'] = ResumeModel.objects.order_by('-id')
		return context

def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('dashboard')
		else:
			context['registration_form'] = form
	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'register.html', context)

def logout_view(request):
	logout(request)
	return redirect('/')

def account_view(request):
	if not request.user.is_authenticated:
			return redirect("login")
	context = {}
	if request.POST:
		form = AccountUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.initial = {
					"email": request.POST['email'],
					"username": request.POST['username'],
			}
			form.save()
			context['success_message'] = "Updated"
	else:
		form = AccountUpdateForm(
			initial={
					"email": request.user.email, 
					"username": request.user.username,
				}
			)
	context['account_form'] = form
	return render(request, "account.html", context)

