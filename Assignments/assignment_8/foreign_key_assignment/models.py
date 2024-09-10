from django.db import models


# Task 1
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


# Task 2
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    grade = models.IntegerField()

    def _str_(self):
        return self.full_name

    def get_courses(self):
        return Course.objects.filter(students=self)


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    students = models.ManyToManyField(Student)

    def _str_(self):
        return self.name
