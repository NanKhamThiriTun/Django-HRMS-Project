from django.shortcuts import render, redirect

# Create your views here.
from .models import PayrollModel
from .forms import PayrollForm
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.core.paginator import Paginator

def search_by(request):
    search = request.GET.get('search')
    if search:    
        payrolls = PayrollModel.objects.filter(
            Q(name__icontains=search) | 
            Q(salary__icontains=search) |
            Q(ot_rate__icontains=search) |
            Q(allowance__icontains=search) |
            Q(deduction__icontains=search) |
			Q(status__icontains=search) 
        )
    else:      
        payrolls = PayrollModel.objects.all()
    return render(request, 'payroll_list.html', {'all_payrolls': payrolls})

def order_by(request):
    order = request.GET.get('order')
    payrolls = PayrollModel.objects.all().order_by("-"+ order)
    if not order:
        order = 'default_field'
    order_selected = {str(order): 'btn-primary text-white'}
    paginator = Paginator(payrolls, 2) # Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'job_list.html', {'page_obj': page_obj, 'order_selected': order_selected})

@permission_required('hr_payrolls.view_payrollmodel', login_url='login')
def payroll(request, payroll_id):
	if request.method == "GET":
		payroll = PayrollModel.objects.get(id=payroll_id)
		return render(request,'payroll_detail.html', {'payroll': payroll})

@login_required(login_url='login')
def all_payrolls(request):
	print('all_payrolls call')
	if request.method == "GET":
		print('all_payrolls GET call')
		all_payrolls = PayrollModel.objects.all()
		paginator = Paginator(all_payrolls, 2) # Show 2 contacts per page.
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		return render(request,'payroll_list.html', {'page_obj': page_obj})

@permission_required('hr_payrolls.add_payrollmodel', login_url='login')
def add_payroll(request):
	print('add_payroll call')
	if request.method == "GET":
		print('add_payroll GET call')
		form = PayrollForm()
		return render(request,'payroll_create.html',{'form':form})
	if request.method == "POST" and request.FILES['attachment']:
		print('add_payroll POST call')
		print('data => ', request.POST)
		form = PayrollForm(request.POST, request.FILES)
		if form.is_valid():
			print('form is valid')
			form.save()
			return redirect('/hr_payrolls/show_payroll/')

@permission_required('hr_payrolls.change_payrollmodel', login_url='login')
def update_payroll(request, payroll_id):
	print('update_payroll call')
	print('payroll_id ', payroll_id)
	payroll = PayrollModel.objects.get(id=payroll_id)
	if request.method == "GET":
		print('update_payroll GET call')
		form = PayrollForm(instance=payroll)
		return render(request, 'payroll_update.html', {'form': form, 'uploaded_image': payroll.attachment})
	elif request.method == "POST":
		print('update_payroll POST call')
		print('data => ', request.POST)
		form = PayrollForm(request.POST, request.FILES, instance=payroll)
		if form.is_valid():
			print('form is valid')
			form.save()
			return redirect('/hr_payrolls/detail/' + str(payroll_id) + '/')

@permission_required('hr_payrolls.delete_payrollmodel', login_url='login')
def delete_payroll(request, payroll_id):
	if request.method == "GET":
		payroll = PayrollModel.objects.get(id=payroll_id)
		payroll.delete()
		return redirect('/hr_payrolls/show_payroll/')