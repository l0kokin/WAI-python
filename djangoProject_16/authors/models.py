from django.db import models

# Create your models here.
class Author(models.Model):
    fullname = models.CharField(max_length=100)
    born_date = models.DateField()