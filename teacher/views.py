from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from course.models import Teacher

@login_required
def teacher_details(request, id):
    teacher = Teacher.objects.get(id=id)
    return render(request, 'teacher_detail.html', {'teacher': teacher})


def teacher_delete(request, id):
    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    return redirect('teachers')




