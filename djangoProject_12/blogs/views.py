from django.shortcuts import render

from blogs.models import Blog


def blogs_list(request):
    # blogs = Blog.objects.all()
    # context = {'blogs': blogs}
    return render(request, 'blogs/blogs_list.html')