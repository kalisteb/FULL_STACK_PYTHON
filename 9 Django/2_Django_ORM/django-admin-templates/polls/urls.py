from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes', views.clientes, name='clientes'),
    path('sitios', views.sitios, name='sitios'),
    path('oportunidades', views.oportunidades, name='oportunidades'),
    path('documentos', views.documentos, name='documentos'),
    path('libros_publicadores', views.libros_publicadores, name='libros_publicadores'),
    path('get_publicador', views.get_publicador, name='get_publicador'),
    path('edit_publicador', views.edit_publicador, name='edit_publicador'),
]