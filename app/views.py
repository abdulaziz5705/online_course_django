from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')

def base(request):
    user = User.objects.all()
    cotnext = {'user': user}
    return render(request, 'base/base.html', context=cotnext)

@login_required
def about(request):
    return render(request, 'about.html')


@login_required
def contact(request):
    return render(request, 'contact.html')


@login_required
def blog(request):
    return render(request, 'blog.html')


@login_required
def courses(request):
    return render(request, 'course.html')


@login_required
def single(request):
    return render(request, 'single.html')


@login_required
def teachers(request):
    return render(request, 'teacher.html')


