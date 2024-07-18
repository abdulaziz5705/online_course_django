from django.urls import path
from .views import courses_list_view, course_create_view
urlpatterns = [
    path('course/', courses_list_view, name='course-list'),
    path('course/create/', course_create_view, name='course-create'),


]