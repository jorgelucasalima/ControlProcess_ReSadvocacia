from django.urls import path
from .views import list_previdenciarios, create_previdenciario, update_previdenciario, delete_previdenciario

urlpatterns = [

    path('', list_previdenciarios, name='list_previdenciarios'),
    path('new', create_previdenciario, name='create_previdenciario'),
    path('update/<int:id>', update_previdenciario, name='update_previdenciario'),
    path("delete/<int:id>/", delete_previdenciario, name='delete_previdenciario'),

]


