from django.shortcuts import render
from .models import Blog

def blog_view(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs, "specialitys": specialitys})

