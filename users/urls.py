from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("login", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("change_password", auth_views.PasswordChangeView.as_view(template_name="users/change_password.html"), name="change_password"),
    path("password_change_done", auth_views.PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"), name="password_change_done"),
    path("reset_password", auth_views.PasswordResetView.as_view(template_name="users/reset_password.html"), name="reset_password"),
    path("password_reset_complete", auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name="password_reset_complete"),
    #path("login", views.login, name="login"),
    #path("change_password", views.change_password, name="change_password"),
    #path("reset_password", views.reset_password, name="reset_password"),

    path('user_dir', views.user_dir, name='user_dir'),
    path('admin_dir', views.admin_dir, name='admin_dir'),
    path('staff_dir', views.staff_dir, name='staff_dir'),
    path('student_dir', views.student_dir, name='student_dir'),
]

