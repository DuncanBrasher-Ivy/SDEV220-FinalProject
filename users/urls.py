
from django.urls import path
from . import views


urlpatterns = [
    path('user_dir', views.user_list, name='user_list'),
    path('admin_dir', views.admin_list, name='admin_list'),
    path('', views.admin_list, name='admin_list'),
]


