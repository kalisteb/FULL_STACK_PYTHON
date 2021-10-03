from django.urls import path, include
from . import views


# todas las rutas de la app
# '' me redirige el view  al metodo o funcion login
urlpatterns = [
    path('', views.login),
    path('registrar', views.registrar),
    path('inicio', views.inicio),
    path('registro', views.registro),
    path('logout', views.logout),
]