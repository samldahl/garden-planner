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
    path('accounts/signup/', views.signup, name='signup'),
]
