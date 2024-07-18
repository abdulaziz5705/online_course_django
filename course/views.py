from django.shortcuts import render, redirect
from .models import Course, Speciality
from .forms import CourseForm


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
            return render(request, 'course_create.html', {'form': form, "message_error": "Error!"})

    form = CourseForm()
    return render(request, 'course_create.html', {'form': form})


