from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def book(request):
	context = {
		"books_list":Book.objects.all(),
	}
	return render(request, "add_book.html", context)


def add_book(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['description']
        book = Book.objects.create(title=title, desc=desc)
    return redirect("books")


def book_view(request, id_book=1):
	book = Book.objects.get(id=id_book)
	context = {
		"book": book,
		"authors_list": book.author.all(),
		"other_authors": Author.objects.exclude(id__in=book.author.all()),
	}
	return render(request, "books.html", context)


def add_author_relation(request):
	values = request.POST['author'].split('|')
	book = Book.objects.get(id=values[0])
	author = Author.objects.get(id=values[1])
	book.author.add(author)
 
	return redirect("/books/"+values[0])


def author(request):
	context = {
		"authors_list":Author.objects.all(),
	}
	return render(request, "add_author.html", context)


def add_author(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        notes = request.POST['notes']
        author = Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)
	
    return redirect("authors")


def author_view(request, id_author=1):
	author = Author.objects.get(id=id_author)
	context = {
		"author": author,
		"books_list": author.books.all(),
		"other_books": Book.objects.exclude(id__in=author.books.all()),
	}
	return render(request, "authors.html", context)

def add_book_relation(request):
	values=request.POST['author'].split('|')
	author=Author.objects.get(id=values[0])
	book=Book.objects.get(id=values[1])
	author.books.add(book)
 
	return redirect("/authors/"+values[0])