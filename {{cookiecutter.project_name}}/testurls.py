"""
test URL Configuration for {{cookiecutter.project_slug}} development
"""
from django.conf.urls import include, url
from django.contrib import admin
import juntagrico

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('juntagrico.urls')),
    url(r'^', include('{{cookiecutter.project_slug}}.urls')),
    url(r'^$', juntagrico.views.home),
]
