from django.shortcuts import render, redirect
from django.contrib import messages
from login.models import User, Autor, Libro,Review


# Create your views here.
def home(request):
    if 'user_id' not in request.session:
        return redirect('login')

    context = {
        "active_user": User.objects.get(id=request.session['user_id']),
        "reverse_list": Libro.objects.all().order_by('id').reverse(),
        "lista_libros": Libro.objects.all().order_by('titulo'),
    }

    return render(request, 'home.html', context)


def add(request):
    context ={
        'autores': Autor.objects.all(),
    }
    return render(request, 'add.html', context)


def insertar(request):
    # Rescatando la info desde el Review
    # con variables errores, vamos a capturar errores
    errores = {}

    if len(request.POST['titulo']) == 0:    
        errores['titulo'] = "Debe ingresar un Título"
        
    if int(request.POST['sautor']) == 0 and len(request.POST['autor']) == 0:
        errores['autor'] = "Debe ingresar un Autor" 
        
    if len(request.POST['review']) == 0:
        errores['review'] = "Debe ingresar una Reseña"
        
    if int(request.POST['rating']) == 0:
        errores['rating'] = "Debe seleccionar una Calificación"
        
    if len(errores) > 0:
        for key, msg in errores.items():
            messages.error(request, msg)
        return render(request, 'add.html')
    
    else:
        if int(request.POST['sautor']) != 0:
        # Si es distinto de 0, viene el autor y tendremos que ir a buscarlo
            autor = Autor.objects.get(id=request.POST['sautor'])
            
        elif len(request.POST['autor']) != 0:
            autores = Autor.objects.all()
            registered_author = 0
            for autor_guardado in autores:
                if autor_guardado.nombre.lower() == request.POST['autor'].lower():
                    registered_author = autor_guardado.id
            if registered_author > 0:
                autor = Autor.objects.get(id=registered_author)
            else:
                autor = Autor.objects.create(nombre=request.POST['autor'].capitalize())
                
        
        book = Libro.objects.create(titulo = request.POST['titulo'], autor = autor, rating = request.POST['rating'])
        Review.objects.create(usuario = User.objects.get(id=request.session['user_id']), contenido = request.POST['review'], libro = book)
        return redirect('/books')



def recuperar(request):
    reg_user = User.objects.get(id=request.session['user_id'])

    context = {
        "active_user": reg_user,
    }
    return render(request, 'recuperar.html', context)


def cambiar_pass(request):
    reg_user = User.objects.get(id=request.session['user_id'])

    pass_actual = request.POST['pass_actual']
    pass_nueva = request.POST['pass_nueva']
    pass_confirm = request.POST['pass_confirmacion']

    context = {
        "active_user": reg_user,
    }
    return render(request, 'recuperar.html', context)

    #if len(request.POST['pass_actual']) == 0:
    #    messages.error(request, "Debes ingresar tu contraseña actual")
    #    return render(request, 'recuperar.html',context)

    #errores = User.objects.validar_login(request.POST['pass_actual'], reg_user)

    #if len(errores) > 0:
    #    for key, msg in errores.items():
    #        messages.error(request, msg)
    #    return render(request, 'recuperar.html',context)
    
    #if len(request.POST['pass_nueva']) == 0 or len(request.POST['pass_confirmacion']) == 0:
    #    messages.error(request, "Debes ingresar tu nueva contraseña")
    #    return render(request, 'recuperar.html',context)
    #elif request.POST['pass_nueva'] != request.POST['pass_confirmacion']:
    #    messages.error(request, "Las contraseñas no coinciden")
    #    return render(request, 'recuperar.html', context)
    #else:
    #    reg_user[0].password = User.objects.encriptar(request.POST['pass_nueva']).decode('utf-8')
    #    reg_user[0].save()
    #    request.session.flush()
    #    return redirect('/')
    #validar el password actual


def edit(request, libro_id):
    context = {
        'libro': Libro.objects.get(id = libro_id),
        'reviews': Review.objects.filter(libro = Libro.objects.get(id = libro_id)).order_by('-id')[:3],
    }
    return render(request, 'libro.html', context)

def add_review(request):
    review = Review.objects.create(
        usuario = User.objects.get(id=request.session['user_id']),
        contenido = request.POST['review'],
        libro = Libro.objects.get(id = request.POST['libro_id']),
        rating = request.POST['rating']
    )
    return redirect(f"/libros/{request.POST['libro_id']}")