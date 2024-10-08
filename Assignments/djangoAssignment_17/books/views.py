from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from books.models import Book
from books.serializers import BookSerializer


# Create your views here.
class BookListView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
