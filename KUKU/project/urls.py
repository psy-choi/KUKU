"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("/", views.home, name="home"),
    path("admin/", admin.site.urls),
    path("home/", views.home, name="home"),
    path("ranking/", views.ranking, name="ranking"),
    path("pictures/<str:category>/<str:search>", views.pictures, name="pictures"),
    path("post/", views.post, name="post"),
    path("like/<int:picture_id>", views.like, name="like"),
    path("post/<str:category>/<str:title>/<str:address>/<str:phone>/", views.post, name="post_upload"),
]
