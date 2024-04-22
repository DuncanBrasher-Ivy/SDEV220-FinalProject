from django.urls import path
from . import views


urlpatterns = [
    path('user_dir', views.user_dir, name='user_dir'),
    path('admin_dir', views.admin_dir, name='admin_dir'),
    path('staff_dir', views.staff_dir, name='staff_dir'),
    path('student_dir', views.student_dir, name='student_dir'),
]

