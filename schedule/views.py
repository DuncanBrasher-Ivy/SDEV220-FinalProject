from django.shortcuts import render


def schedule(request):
    user = None
    return render(request, 'schedule/schedule.html', {'logged_in': user})

