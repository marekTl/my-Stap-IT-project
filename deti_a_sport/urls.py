"""
URL configuration for deti_a_sport project.

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
from rezervacni_system.views import prihlasit_se, uvod

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', uvod, name='uvod'),
    path('registrace/', prihlasit_se, name='prihlaska'),
    path('registrace/', include('rezervacni_system.urls'))
]
