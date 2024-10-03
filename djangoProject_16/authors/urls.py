from django.urls import path

from authors.views import authors_list, author_detail

urlpatterns = [
    path('', authors_list, name='index'),
    path('<int:pk>/', author_detail, name='author-detail'),
]