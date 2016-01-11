"""ProyectoJA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from blog import views

urlpatterns = [
                  url(r'^admin/', include(admin.site.urls)),
                  url(r'^noticia/', include('blog.urls')),
                  url(r'^cate/', include('blog.urls')),
                  url(r'^com/', include('blog.urls')),
                  url(r'^search/', views.search),
                  url(r'^categoria/(?P<cat>\d+)$', views.categoria, name='Categorias'),
                  url(r'^autor/(?P<aut>\d+)$', views.autor, name='Autor'),
                  url(r'^users/', include('Users.urls', namespace="users")),
                  url(r'^$', views.index, name='index'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
