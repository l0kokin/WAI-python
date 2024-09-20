from django.db import models
from datetime import date
from django.utils import timezone


# Task 1
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def num_books(self):
        return self.book_set.count()


class Book(models.Model):
    title = models.CharField(max_length=100)
    date_published = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Task 2
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    grade = models.IntegerField()

    def __str__(self):
        return self.full_name

    def get_courses(self):
        return Course.objects.filter(students=self)

    # Task 3
    def calc_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        return age


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
