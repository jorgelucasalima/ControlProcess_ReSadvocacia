from django.urls import path
from .views import list_civels, create_civel, update_civel, delete_civel


urlpatterns = [

    path('', list_civels, name='list_civels'),
    path('new', create_civel, name='create_civel'),
    path('update/<int:id>', update_civel, name='update_civel'),
    path("delete/<int:id>/", delete_civel, name='delete_civel'),


]