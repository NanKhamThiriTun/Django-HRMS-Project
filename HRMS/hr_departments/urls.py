from django.urls import path
from hr_departments import views

urlpatterns = [
	path('show_department/', views.AllDepartments.as_view()),
	path('new_department/', views.AddDepartment.as_view()),
	path('update/<int:department_id>/', views.UpdateDepartment.as_view()),
	path('detail/<int:department_id>/', views.Department.as_view()),
	path('delete/<int:department_id>/', views.DeleteDepartment.as_view()),
	path('search_by/', views.SearchBy.as_view()),
	path('order_by/', views.OrderBy.as_view())
	# path('path_name', file_name.class_name.as_view())
]