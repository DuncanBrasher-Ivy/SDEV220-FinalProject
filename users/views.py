from django.shortcuts import render
from .models import IvyMeshUser


def user_list(request):
    users = IvyMeshUser.objects.filter(is_superuser=False)
    return render(request, 'users/user_list.html', {'users': users})

def admin_list(request):
    adminusers = IvyMeshUser.objects.filter(is_superuser=True)
    return render(request, 'users/admin_list.html', {'adminusers': adminusers})

