from . import views
from django.urls import path

urlpatterns = [
        path('', views.dogs_profile, name='dogs_profile'),
]