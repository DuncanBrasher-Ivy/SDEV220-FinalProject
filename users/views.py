from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User


@login_required
def base_user_dir(request, fp, users):
    return render(request, fp, {'users': users})

def user_dir(request):
    users = User.objects.filter(is_superuser=False)
    return base_user_dir(request, 'users/user_dir.html', users)

@staff_member_required
def admin_dir(request):
    adminusers = User.objects.filter(is_superuser=True)
    return base_user_dir(request, 'users/admin_dir.html', adminusers)

def staff_dir(request):
    users = User.objects.filter(is_superuser=False, is_staff=True)
    return base_user_dir(request, 'users/staff_dir.html', users)

def student_dir(request):
    users = User.objects.filter(is_staff=False)
    return base_user_dir(request, 'users/student_dir.html', users)

