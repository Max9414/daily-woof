from . import views
from django.urls import path

urlpatterns = [
    path('', views.BreedsList.as_view(), name='breeds'),
    path('<int:id>/', views.breed_detail, name='breed_detail'),
]