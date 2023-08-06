from django.urls import path
from hr_jobs import views

urlpatterns = [
	path('show_job/', views.all_jobs),
	path('new_job/', views.add_job),
	path('update/<int:job_id>/', views.update_job),
	path('detail/<int:job_id>/', views.job),
	path('delete/<int:job_id>/', views.delete_job),
	path('search_by/', views.search_by),
	path('order_by/', views.order_by)
	# path('path_name/', file_name.function_name)
]