from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Course, Speciality
from .forms import CourseForm, TeacherFrorm, CourseUpdateForm

def courses_list_view(request):
    courses = Course.objects.all()
    specialitys = Speciality.objects.all()
    context = {
        "courses": courses,
        "specialitys": specialitys,
    }
    return render(request, 'course.html', context)


def course_create_view(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course-list')
        else:
            return render(request, 'course/course_create.html', {'form': form, "message_error": "Error!"})

    form = CourseForm()
    return render(request, 'course/course_create.html', {'form': form})


@login_required
def course_detail_view(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'course/course_detail.html', {"course": course})


def course_delete_view(request, id):
    course_delete = Course.objects.get(id=id)
    course_delete.delete()
    return redirect('course-list')


def teacher_create(request):
    if request.method == "POST":
        form = TeacherFrorm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher')
        else:
            return render(request, 'create_teacher.html', {'form': form, "message_error": "Error!"})

    form = TeacherFrorm()
    return render(request, 'create_teacher.html', {'form': form})


def course_update(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == "POST":
        form = CourseUpdateForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course-detail', pk=course.pk)

    course = Course.objects.get(pk=pk)
    return render(request, 'course_update.html', context={'course': course})
