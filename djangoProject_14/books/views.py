
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from books.forms import BookForm
from books.models import Book


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/books_create.html'
    success_url = reverse_lazy('books-list')


# def create_book(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Success')
#     else:
#         form = BookForm()
#         return render(request, 'books/books_create.html', {'form': form})


class BookListView(ListView):
    model = Book
    template_name = 'books/books_list.html'
    context_object_name = 'books'


# def list_books(request):
#     books = Book.objects.all()
#     return render(request, 'books/books_list.html', {'books': books})


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/books_detail.html'
    context_object_name = 'book'


# def detail_book(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     return render(request, 'books/books_detail.html', {'book': book})


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/books_update.html'
    success_url = reverse_lazy('books-list')
    context_object_name = 'book'


# def update_book(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'POST':
#         form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Success')
#     else:
#         form = BookForm(instance=book)
#     return render(request, 'books/books_update.html', {'form': form})


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/books_delete.html'
    success_url = reverse_lazy('books-list')
    context_object_name = 'book'


# def delete_book(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'POST':
#         book.delete()
#         return HttpResponse('Success')
#     return render(request, 'books/books_delete.html', {'book': book})
