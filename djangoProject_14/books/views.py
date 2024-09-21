from django.http import HttpResponse
from django.shortcuts import render

from books.forms import BookForm
from books.models import Book


# Create your views here.
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Success')
        else:
            form = BookForm()
            return render(request, 'books/books_create.html', {'form': form})


def list_books(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books': books})


def detail_book(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, )
