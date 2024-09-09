from django.db import models
from pip._vendor.rich.markup import Tag


class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_published = models.DateTimeField()
    content = models.TextField()
    # this here or blogs in the Tag class
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title


# Django will create this automatically, since this is a common use case.
# class BlogTag(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.tag} {self.blog}"


class Tag(models.Model):
    name = models.CharField(max_length=100)
    # this or tag in the Blog class
    # blogs = models.ManyToManyField('Blog')

    def __str__(self):
        return self.name


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.content