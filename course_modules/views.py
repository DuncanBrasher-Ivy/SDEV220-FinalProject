from django.shortcuts import render


def course_modules(request):
    user = None
    return render(request, 'course_modules/course_modules.html', {'logged_in': user})

