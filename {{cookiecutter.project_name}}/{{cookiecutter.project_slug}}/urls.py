from django.urls import path
from {{cookiecutter.project_slug}} import views

app_name = '{{cookiecutter.project_initials}}'
urlpatterns = [
    path('{{cookiecutter.project_initials}}/home', views.home, name='home')
]
