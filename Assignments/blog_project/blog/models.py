from django.db import models


# from datetime import date

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField()
    category = models.CharField(max_length=200)
