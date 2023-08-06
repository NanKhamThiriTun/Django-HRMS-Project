from django.urls import path
from hr_employees import views

urlpatterns = [
    path('show_employee/', views.all_employees),
    path('new_employee/', views.add_employee),
    path('update_employee/<int:employee_id>/', views.update_employee),
    path('detail/<int:employee_id>/', views.employee),
    path('delete/<int:employee_id>/', views.delete_employee),
    path('search_by/', views.search_by),
    path('order_by/', views.order_by)
]