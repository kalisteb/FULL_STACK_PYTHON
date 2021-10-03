from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


def index(request):
    clientes = Client.objects.all()
    context = {
        'client_list' : clientes,
    }
    return render(request, 'polls/home.html', context)


def clientes(request):
    clientes = Client.objects.all()
    context = {
        'client_list' : clientes,
    }
    return render(request, 'polls/cliente.html', context)


def sitios(request):
    sitios = Site.objects.all()
    context = {
        'sites_list' : sitios,
    }
    return render(request, 'polls/sites.html', context)


def oportunidades(request):
    oportunidades = Lead.objects.all()
    context = {
        'leads_list' : oportunidades,
    }
    return render(request, 'polls/leads.html', context)


def documentos(request):
    documentos = Documento.objects.all()
    context = {
        'documents_list' : documentos,
    }
    return render(request, 'polls/documents.html', context)


def libros_publicadores(request):

    libros = Libro.objects.all()
    publicadores = Publicador.objects.all()
    context = {
        'lista_libros' : libros,
        'lista_publicadores' : publicadores,
    }
    return render(request, 'polls/libros_publicadores.html', context)

def get_publicador(request):
    libros = Libro.objects.all()
    if 'id' in request.POST: #Si existe 'publicador' en request.POST...
        publicador = Publicador.objects.filter(id=request.POST['id']) #Consulto por el objeto con ese 'id'
        context = {
            'lista_libros' : libros,
            'publicador' : publicador,
        }
        return render(request, 'polls/edit_publicador.html', context)
    return redirect('libros_publicadores')


def edit_publicador(request):
    libros = Libro.objects.all()
    if 'id' in request.POST: # Hago click en "Guardar"
        publicador = Publicador.objects.filter(id=request.POST['id']) #Llamo al publicador segun el id que trae request.POST
        for libro in libros: # recorro la lista de todos los libros
            key = f'libro-{libro.id}' # preparo la 'key' para consultar por ella en el request.POST
            if key in request.POST: # Pregunto si está la key en request.POST
                if not libro in publicador[0].libros.all(): # si no está el libro entre los libros del publicador
                    publicador[0].libros.add(libro) # Añado el libro en request.POST
            else:           #pero si no está la key en request.POST
                if libro in publicador[0].libros.all(): # Y además está el libro entre los libros del publicador
                    publicador[0].libros.remove(libro) #Elimino el libro de entre los libros del publicador
    return redirect('libros_publicadores')