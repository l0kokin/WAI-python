from rest_framework.routers import DefaultRouter
from django.urls import path, include
from books.views import  BookListView

router = DefaultRouter()
router.register(r'books', BookListView)

urlpatterns = [
    path('', include(router.urls)),
]
