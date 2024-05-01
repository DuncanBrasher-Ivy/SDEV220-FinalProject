from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def course_modules(request):
    return render(request, 'course_modules/course_modules.html')

