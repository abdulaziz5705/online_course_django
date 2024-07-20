from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from course.models import Course, Teacher


def index(request):
    courses = Course.objects.all()
    teachers = Teacher.objects.all()
    return render(request, 'index.html', {'courses': courses, 'teachers': teachers})


def base(request):
    user = User.objects.all()
    cotnext = {'user': user}
    return render(request, 'base/base.html', context=cotnext)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def blog(request):
    return render(request, 'blog.html')


def courses(request):
    courses = Course.objects.all()
    return render(request, 'course/course.html', {'courses': courses})


@login_required
def single(request):
    return render(request, 'single.html')


def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher.html', {'teachers': teachers})


