from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def random_word(request):
    if "contador" not in request.session.keys():
        request.session['contador'] = 0
    else:
        request.session['contador'] += 1
    context = {
        "contador": request.session['contador'],
        "cadena": get_random_string(length=14)
    }
    return render(request, "index.html", context)

def reset(request):
    request.session['contador'] = 0
    return render(request, "index.html")