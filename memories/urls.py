from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_memory, name='add_memory'),
    path('edit/<int:pk>/', views.edit_memory, name='edit_memory'),
]