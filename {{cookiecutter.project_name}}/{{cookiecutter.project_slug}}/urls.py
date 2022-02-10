from django.urls import path
from {{cookiecutter.project_slug}} import views

urlpatterns = [
    path('{{cookiecutter.project_initials}}/home', views.home)
]
