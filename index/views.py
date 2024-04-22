from django.shortcuts import render


def index(request):
    user = None
    return render(request, 'index/index.html', {'logged_in': user})

