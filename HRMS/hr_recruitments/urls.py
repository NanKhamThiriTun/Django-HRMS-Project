from django.urls import path
from hr_recruitments import views

urlpatterns = [
	path('show_resume/', views.ResumeListView.as_view(), name='resume_list'),
	path('new_resume/', views.ResumeCreateView.as_view(), name='resume_create'),
	path('update/<int:pk>/', views.ResumeUpdateView.as_view(), name='resume_update'),
	path('detail/<int:pk>/', views.ResumeDetailView.as_view(), name='resume_detail'),
	path('delete/<int:pk>/', views.ResumeDeleteView.as_view(), name='resume_delete'),
	# path('search_by/', views.SearchBy.as_view()),
	# path('order_by/', views.OrderBy.as_view())
]