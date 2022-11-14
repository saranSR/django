from django import views
from django.contrib import admin
from django.urls import include, path
from .views import index, add_item,delete_item, edit_item, update_item
    
urlpatterns = [
    path('', index,name='index'),
    path('index', index,name='index'),
    path('add_item', add_item, name='add_item'),
    path('delete_item/<int:myid>/', delete_item, name='delete_item'),
    path('update_item/<int:myid>/', update_item, name='update_item'),
    path('edit_item/<int:myid>/', edit_item, name='edit_item'),
    
]