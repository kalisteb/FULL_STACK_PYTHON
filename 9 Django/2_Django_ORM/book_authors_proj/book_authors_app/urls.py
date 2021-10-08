from django.urls import path
from . import views

urlpatterns = [
    path('', views.book, name='books'),
    path('add_book', views.add_book, name='add_book'),
    path('books/<int:id_book>', views.book_view),
    path('books/add_author_relation', views.add_author_relation, name='add_author_relation'),
    path('authors', views.author, name='authors'),
    path('add_author', views.add_author, name='add_author'),
	path('authors/<int:id_author>', views.author_view),
	path('authors/add_book_relation', views.add_book_relation, name='add_book_relation'),
]