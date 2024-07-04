"""
URL configuration for my_dj_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
import India
from India.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('India/',include("India.urls")),
    path('Andhra_Pradesh/',Andhra_Pradesh,name='Andhra_Pradesh'),
    path('Telangana/',Telangana,name='Telangana'),
    path('TamilNadu/',TamilNadu,name='TamilNadu'),
    path('Karnataka/',Karnataka,name='Karnataka'),
    path('Kerala/',Kerala,name='Kerala'),
    path('Maharastra/',Maharastra,name='Maharastra'),
    path('Orissa/',Orissa,name='Orissa'),
]
