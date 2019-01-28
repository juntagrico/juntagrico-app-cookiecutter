from django.conf.urls import url
from {{cookiecutter.project_slug}} import views

urlpatterns = [
    url(r'^{{cookiecutter.project_initials}}/home$', views.home)
]
