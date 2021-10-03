from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from login.models import *



# Create your views here.
def home(request):
    active_user = User.objects.get(id=request.session['user_id'])
    lista_usuarios = User.objects.all()
    
    #buscar donde el usuario es receptor para obtener el historial
    mis_pokes=[]
    #diccionario
    poke_user = Poke.objects.filter(receptor = active_user).values('emisor').annotate(total=Count('emisor')).order_by('-total')#.reverse() para orden descendente o usar signo -
    #{'emisor': 1, 'total': 1} ejemplo
    for user in poke_user:
        mis_pokes.append(
            {
            "emisor":User.objects.filter(id=user["emisor"]), #queryset
            "total":user["total"]
            }
        )
    
    context = {
        "active_user": active_user,
        "lista_usuarios": lista_usuarios,
        "mis_pokes" : mis_pokes, #arreglo de diccionarios
        "poke_user" : poke_user,      
    }

    return render(request, 'home.html', context)


def addpoke(request):
    receptor=User.objects.get(id=request.POST['receptor_id'])
    emisor= User.objects.get(id=request.session['user_id'])
    receptor.historico +=1 #suma un toque al usuario receptor
    receptor.save()

    poke= Poke.objects.create(receptor=receptor, emisor=emisor)
    #toque= Toque.objects.create(receptor=receptor_id, emisor=emisor_id)
    
    return redirect('/home')


