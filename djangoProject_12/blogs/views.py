from django.shortcuts import render

from blogs.models import Blog


def blogs_list(request):
    all_blogs = Blog.objects.all()
    context = {
        'blogs': all_blogs,
    }
    return render(request, 'blogs/blogs_list.html', context=context)