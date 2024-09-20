from django.shortcuts import render
from my_app.models import Book


# Create your views here.
def book_list(request):
    all_books = Book.objects.all()
    context = {
        'books': all_books
    }
    return render(request, 'books/book_list.html', context=context)
