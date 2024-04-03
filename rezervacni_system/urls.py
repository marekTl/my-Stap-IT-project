from django.urls import path
from .import views

urlpatterns = [
    path('uspesna_registrace', views.uspesna_registrace, name='uspesna_registrace')
]