from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name

    def num_books(self):
        return self.book_set.count()


class Book(models.Model):
    title = models.CharField(max_length=100)
    date_published = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def _str_(self):
        return self.title
