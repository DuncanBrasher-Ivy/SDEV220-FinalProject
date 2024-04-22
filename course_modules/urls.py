from django.urls import path
from . import views


urlpatterns = [
    path('', views.course_modules, name='course_modules'),
]


