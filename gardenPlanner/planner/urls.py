# planner/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gardens/', views.gardens_index, name='gardens-index'),
    path('gardens/new/', views.gardens_create, name='gardens-create'),
    path('gardens/<int:garden_id>/', views.gardens_detail, name='gardens-detail'),
    path('gardens/<int:garden_id>/delete/', views.gardens_delete, name='gardens-delete'),
    path('gardens/<int:garden_id>/plants/new/', views.plants_create, name='plants-create'),
    path('plants/<int:plant_id>/', views.plants_detail, name='plants-detail'),
    path('plants/<int:plant_id>/delete/', views.plants_delete, name='plants-delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
