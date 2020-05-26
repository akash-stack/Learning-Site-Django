"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import include
from schoolsite import views

urlpatterns = [
    path('',views.index,name='index'),
    path('sign-in',views.signin,name='profile'),
    path('home-page',views.home,name='home'),
    path('About-page',views.about,name='about'),
    path('contact-page',views.contact,name='contact'),
    path('gallery-page',views.gallery,name='gallery'),
    path('admission-page',views.admission,name='admission'),
    path('program-page',views.program,name='program'),
    path('parents-page',views.parents,name='parents'),
    path('news-page',views.news,name='news'),
    path('schoolsite/',include('schoolsite.url')),
    path('admin/', admin.site.urls),
]
