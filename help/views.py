from django.shortcuts import render


def help(request):
    user = None
    return render(request, 'help/help.html', {'logged_in': user})

