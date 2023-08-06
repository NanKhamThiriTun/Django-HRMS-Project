from django.shortcuts import render, redirect

# Create your views here.
from .models import AttendanceModel
from .forms import AttendanceForm
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime

def search_by(request):
	search = request.GET.get('search')
	if search:    
		attendances = AttendanceModel.objects.filter(
			Q(name__icontains=search) | 
			Q(sign_in__icontains=search) |
			Q(sign_out__icontains=search) 
		)
	else:      
		attendances = AttendanceModel.objects.all()
	return render(request, 'attendance_list.html', {'all_attendances': attendances})

def order_by(request):
	order = request.GET.get('order')
	attendances = AttendanceModel.objects.all().order_by("-"+ order)
	if not order:
		order = 'default_field'
	order_selected = {str(order): 'btn-primary text-white'}
	paginator = Paginator(attendances, 2) # Show 2 contacts per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	return render(request, 'attendance_list.html', {'page_obj': page_obj, 'order_selected': order_selected})

@login_required(login_url='login')
def all_attendances(request):
	print('all_attendances call')
	if request.method == "GET":
		print('all_attendances GET call')
		all_attendances = AttendanceModel.objects.all()
		paginator = Paginator(all_attendances, 2) # Show 2 contacts per page.
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		return render(request,'attendance_list.html', {'page_obj': page_obj})


@permission_required('hr_attendances.view_attandancemodel', login_url='login')
def attendance(request, attendance_id):
	if request.method == "GET":
		attendance = AttendanceModel.objects.get(id=attendance_id)
		return render(request,'attendance_detail.html', {'attendance': attendance})

@permission_required('hr_attendances.add_attandancemodel', login_url='login') 
def add_attendance(request):
	print('add_attendance call')
	if request.method == "GET":
		print('add_attendance GET call')
		form = AttendanceForm()
		return render(request,'attendance_create.html',{'form':form})
	if request.method == "POST":
		print('add_attendance POST call')
		print('data => ', request.POST.get('sign_out'))
		name = request.POST.get('name')
		sign_in = request.POST.get('sign_in')
		sign_out = request.POST.get('sign_out')
		employee = request.POST.get('employee')
		
		if request.POST.get('is_active') == 'on':
			is_active = True
		else:
			is_active = False
		Attendance = AttendanceModel.objects.create(
			name = name,
			sign_in = sign_in,
			sign_out = sign_out,
			employee = employee,
			is_active = is_active
		)
		Attendance.save()
		return redirect('/hr_attendances/show_attendance/')

@permission_required('hr_attendances.change_attendancemodel', login_url='login')  
def update_attendance(request, attendance_id):
	print('update_attendance call')
	print('attendance_id ', attendance_id)
	attendance= AttendanceModel.objects.get(id=attendance_id)
	if request.method == "GET":
		print('update_attendance GET call')
		values = {
			'name': attendance.name,
			'sign_in': datetime.strftime(attendance.sign_in, '%Y-%m-%dT%H:%M'),
			'sign_out': datetime.strftime(attendance.sign_out, '%Y-%m-%dT%H:%M'),
			'is_active': attendance.is_active,
			'employee': attendance.employee,
			
		}
		
		print('get form ', values)
		context = {'form': values, 'attendance': attendance}
		return render(request, 'attendance_update.html', context)
	elif request.method == "POST":
		attendance = AttendanceModel.objects.get(id=attendance_id)
		attendance.name = request.POST.get('name')
		attendance.sign_in = request.POST.get('sign_in')
		attendance.sign_out = request.POST.get('sign_out')
		if request.POST.get('is_active') == "on":
			attendance.is_active = True
		else:
			attendance.is_active = False
		attendance.employee = request.POST.get('employee')
		attendance.save()
		return redirect('/hr_attendances/detail/' + str(attendance_id) + '/')

@permission_required('hr_attendances.delete_changemodel', login_url='login') 
def delete_attendance(request, attendance_id):
	if request.method == "GET":
		attendance = AttendanceModel.objects.get(id=attendance_id)
		attendance.delete()
		return redirect('/hr_attendances/show_attendance/')