from django.urls import path
from hr_expenses import views

urlpatterns = [
	path('show_expense/', views.all_expenses),
	path('new_expense/', views.add_expense),
	path('update/<int:expense_id>/', views.update_expense),
	path('detail/<int:expense_id>/', views.expense),
	path('delete/<int:expense_id>/', views.delete_expense),
	path('search_by/', views.search_by),
	path('order_by/', views.order_by)
	# path('path_name/', file_name.function_name)
]