from django.urls import path
from .views import index, about, blog, contact, courses, single, teachers


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('course/', courses, name='course'),
    path('single/', single, name='single'),
    path('teachers/', teachers, name='teachers'),
    path('blog/', blog, name='blog'),
]
