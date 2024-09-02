from django.http import HttpResponse
from django.urls import reverse

from mock_data import blogs


def blogs_view(request):
    html = ''
    for key, blog in blogs.items():
        blog_details_url = reverse('blog_details', args=[key])
        html += f"""
        <h3>{blog['title']}</h3>
        <p>By {blog['author']} on {blog['date_published']}</p>
        <p>{blog['content']}</p>
        <p>Tags: {', '.join(blog['content'])}</p>
        <a href=/blogs/{key}>View details</a>
        """
    return HttpResponse(html, status=200)


def blog_details_view(request, blog_key):
    blog = blogs[blog_key]
    comments = ''
    for comment in blog['comments']:
        comments += f'<p>{comment['author']}: {comment['content']} <small>{comment['date']}</small></p>'
    html = f"""
    <h3>Blog Details</h3>
    <p>By {blog['author']} on {blog['date_published']}</p>
    <p>{blog['content']}</p>
    <p>Tags: {', '.join(blog['content'])}</p>
    <hr>
    <p>Comments: {comments}</p>
    """
    return HttpResponse(html, status=200)
