from . import views
from django.urls import path

urlpatterns = [
    path('', views.petcare, name='petcare'),
]