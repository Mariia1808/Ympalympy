"""rnaul URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render
from rnaul_main import views
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt


vue_urls = [
  path('', lambda request: HttpResponse(render(request, 'vue_index.html'))),
  path('another-path/', lambda request: HttpResponse(render(request, 'vue_index.html'))),
]
urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include(vue_urls)),
  url(r'^api/toxicity$', csrf_exempt(views.toxicity_rate)),
]
