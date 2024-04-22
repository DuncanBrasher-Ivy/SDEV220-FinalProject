from django.shortcuts import render
from .models import IvyMeshUser


def base_user_dir(request, fp, users):
    user = None
    return render(request, fp, {'users': users, 'logged_in': user})

def user_dir(request):
    users = IvyMeshUser.objects.filter(is_superuser=False)
    return base_user_dir(request, 'users/user_dir.html', users)

def admin_dir(request):
    adminusers = IvyMeshUser.objects.filter(is_superuser=True)
    return base_user_dir(request, 'users/admin_dir.html', adminusers)

def staff_dir(request):
    users = IvyMeshUser.objects.filter(role="staff")
    return base_user_dir(request, 'users/staff_dir.html', users)

def student_dir(request):
    users = IvyMeshUser.objects.filter(role="student")
    return base_user_dir(request, 'users/student_dir.html', users)


