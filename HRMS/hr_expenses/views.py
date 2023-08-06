from django.shortcuts import render, redirect

# Create your views here.
from .models import ExpenseModel
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.core.paginator import Paginator

def search_by(request):
    search = request.GET.get('search')
    if search:    
        expenses = ExpenseModel.objects.filter(
            Q(name__icontains=search) | 
            Q(quantity__icontains=search) |
            Q(product__icontains=search) |
            Q(price__icontains=search) |
            Q(total__icontains=search) 
        )
    else:      
        expenses = ExpenseModel.objects.all()
    return render(request, 'expense_list.html', {'all_expenses': expenses})

def order_by(request):
    order = request.GET.get('order')
    expenses = ExpenseModel.objects.all().order_by("-"+ order)
    order_selected = {str(order): 'btn-primary text-white'}
    return render(request, 'expense_list.html', {'all_expenses': expenses, 'order_selected': order_selected})

@permission_required('hr_expenses.view_expensemodel', login_url='login')
def expense(request, expense_id):
	if request.method == "GET":
		expense = ExpenseModel.objects.get(id=expense_id)
		return render(request,'expense_detail.html', {'expense': expense})

@login_required(login_url='login')
def all_expenses(request):
	print('all_expenses call')
	if request.method == "GET":
		print('all_expenses GET call')
		all_expenses = ExpenseModel.objects.all()
		paginator = Paginator(all_expenses, 2) # Show 2 contacts per page.
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		return render(request,'expense_list.html', {'page_obj': page_obj})


@permission_required('hr_expenses.add_expensemodel', login_url='login') 
def add_expense(request):
	print('add_expense call')
	if request.method == "GET":
		print('add_expense GET call')
		form = ExpenseForm()
		return render(request,'expense_create.html',{'form':form})
	if request.method == "POST" and request.FILES['attachment']:
		print('add_expense POST call')
		print('data => ', request.POST)
		form = ExpenseForm(request.POST, request.FILES)
		if form.is_valid():
			print('form is valid')
			form.save()
			return redirect('/hr_expenses/show_expense/')

@permission_required('hr_expenses.add_expensemodel', login_url='login') 
def update_expense(request, expense_id):
	print('update_expense call')
	print('expense_id ', expense_id)
	expense = ExpenseModel.objects.get(id=expense_id)
	if request.method == "GET":
		print('update_expense GET call')
		form = ExpenseForm(instance=expense)
		return render(request, 'expense_update.html', {'form': form, 'uploaded_image': expense.attachment})
	elif request.method == "POST":
		print('update_expense POST call')
		print('data => ', request.POST)
		form = ExpenseForm(request.POST, request.FILES, instance=expense)
		if form.is_valid():
			print('form is valid')
			form.save()
			return redirect('/hr_expenses/detail/' + str(expense_id) + '/')

@permission_required('hr_expenses.add_expensemodel', login_url='login') 
def delete_expense(request, expense_id):
	if request.method == "GET":
		expense = ExpenseModel.objects.get(id=expense_id)
		expense.delete()
		return redirect('/hr_expenses/show_expense/')