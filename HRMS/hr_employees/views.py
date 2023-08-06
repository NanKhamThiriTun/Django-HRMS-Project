from django.shortcuts import render,redirect
from .models  import EmployeeModel
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def search_by(request):
    print('search by +++++++++++++++++++++++++++++++++++++++ ')
    search = request.GET.get('search')
    if search:    
        employees = EmployeeModel.objects.filter(
            Q(name__icontains=search) | 
            Q(age__icontains=search) |
            Q(birthday__icontains=search) |
            Q(address__icontains=search) |
            Q(email__icontains=search) |
            Q(gender__icontains=search) |
            Q(joining_date__icontains=search)
        )
    else:      
        employees = EmployeeModel.objects.all()
    return render(request, 'employee_list.html', {'page_obj': employees})

def order_by(request):
    print('order by call +++++++++++++++++++++++++++++++++++++++++++++++++++ ')
    order = request.GET.get('order')
    employees = EmployeeModel.objects.all().order_by("-" + order)
    order_selected = {str(order): 'btn-primary text-white'}
    paginator = Paginator(employees, 2) # Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'employee_list.html', {'page_obj': page_obj, 'order_selected': order_selected})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            return redirect('/employees/show_employee/')
        else:
            return render(request, 'login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        return render(request, 'login.html')
    
def logout_view(request):
    logout(request)
    return redirect('/login')

@permission_required('employees.view_employeemodel', login_url='login')
def add_employee(request):
    print('add_employee ++++++++++++++++++++++++++++++++++++++++ ')
    if request.method == "GET":
        employee = EmployeeModel()
        return render(request,'employee_create.html',{'employee': employee})
    if request.method == "POST" and request.FILES['image']:
        name = request.POST.get('name')
        age = request.POST.get('age')
        birthday = request.POST.get('birthday')
        address = request.POST.get('address')
        email = request.POST.get('email')
        gender = request.POST.get('gender')


        if request.POST.get('is_married') == 'on':
            is_married = True
        else:
            is_married = False
    joining_date = request.POST.get('joining_date')
    image = request.FILES.get('image')

    employee = EmployeeModel.objects.create(
        name=name,
			age=age,
			birthday=birthday,
			address=address,
			email=email,
			gender=gender,
			is_married=is_married,
			joining_date=joining_date,
			image=image
    )
    employee.save()
    return redirect('/employees/show_employee/')

@login_required(login_url='login')
def all_employees(request):
	print('all_employees call ++++++++++++++++++++')
	if request.method == "GET":
		print('all_employees GET call')
		all_employees = EmployeeModel.objects.all()
		paginator = Paginator(all_employees, 2) # Show 2 contacts per page.
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		return render(request,'employee_list.html', {'page_obj': page_obj})

@permission_required('employees.view_employeemodel', login_url='login')
def employee(request, employee_id):
    if request.method == "GET":
        employee = EmployeeModel.objects.get(id=employee_id)
    return render(request,'employee_detail.html', {'employee': employee})

@permission_required('employees.view_employeemodel', login_url='login')
def delete_employee(request, employee_id):
    if request.method == "GET":
        employee = EmployeeModel.objects.filter(id=employee_id)
        employee.delete()
        return redirect('/employees/show_employee/')

@permission_required('employees.view_employeemodel', login_url='login')
def update_employee(request, employee_id):
	print('update_employee call +++++++++++++++++++++')
	print('employee_id ', employee_id)
	employee = EmployeeModel.objects.get(id=employee_id)
	if request.method == "GET":
		print('update_employee GET call')
		employee.birthday = str(employee.birthday)
		employee.joining_date = datetime.strftime(employee.joining_date, '%Y-%m-%dT%H:%M')
		context = {'employee': employee, 'uploaded_image': employee.image}
		return render(request, 'employee_update.html', context)
	elif request.method == "POST":
		print('update_employee POST call')
		print('data => ', request.POST)
		employee.name = request.POST.get('name')
		employee.age = request.POST.get('age')
		employee.birthday = request.POST.get('birthday')
		employee.address = request.POST.get('address')
		employee.email = request.POST.get('email')
		employee.gender = request.POST.get('gender')
		employee.is_married = request.POST.get('is_married')
		if request.POST.get('is_married') == 'on':
			employee.is_married = True 
		else:
			employee.is_married = False
		employee.joining_date = request.POST.get('joining_date')
		if request.FILES.get('image'):
			employee.image = request.FILES.get('image')
		employee.save()
		return redirect('/employees/detail/' + str(employee_id) + '/')
