from django.shortcuts import render, HttpResponse
from .models import Books, Authors

def index(request):
    return render(request, 'index.html')


def authors(request):
    #maneja listado autores
    books = Books.objects.all()
    authors = Authors.objects.all()
    context = {
        'books': books,
        'authors': authors
    }
    return render(request,'authors.html',context)


def books(request):
    books= Books.objects.all()
    authors= Authors.objects.all()
    context= {
        'books': books,
        'authors': authors,
    }
    return render(request,'books.html',context)
    