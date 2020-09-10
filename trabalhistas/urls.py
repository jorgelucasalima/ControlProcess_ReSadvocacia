from django.urls import path
from .views import list_trabalhistas, create_trabalhista, update_trabalhista, delete_trabalhista

urlpatterns = [

    path('', list_trabalhistas, name='list_trabalhistas'),
    path('new', create_trabalhista, name='create_trabalhista'),
    path('update/<int:id>', update_trabalhista, name='update_trabalhista'),
    path("delete/<int:id>/", delete_trabalhista, name='delete_trabalhista'),


]