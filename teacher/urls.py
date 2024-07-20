from django.urls import path
from .views import teacher_details, teacher_delete

urlpatterns = [
    path('teacher/detail/<int:id>/', teacher_details, name='teacher-details'),
    path('teacher/delete/<int:id>/', teacher_delete, name='teacher-delete')
]
