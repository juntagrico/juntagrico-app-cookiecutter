"""
test URL Configuration for {{cookiecutter.project_slug}} development
"""
from django.urls import include, path
from django.contrib import admin
import juntagrico

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('{{cookiecutter.project_slug}}.urls')),
    path('', include('juntagrico.urls')),
    path('', juntagrico.views.home),
]
