from django.shortcuts import render, redirect
from django.contrib import messages
from login.models import User


# Create your views here.
def home(request):
    reg_user = User.objects.get(id=request.session['user_id'])
    lista_usuarios = User.objects.all()
    
    context = {
        "active_user": reg_user,
        "lista_usuarios": lista_usuarios
    }

    return render(request, 'home.html', context)
