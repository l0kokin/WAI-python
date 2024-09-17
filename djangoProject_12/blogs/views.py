from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from blogs.models import Blog


def blogs_list(request):
    all_blogs = Blog.objects.all()
    context = {
        'blogs': all_blogs,
    }
    return render(request, 'blogs/blogs_list.html', context=context)


def blogs_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'blogs/blogs_detail.html', context=context)
