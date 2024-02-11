from django.urls import path
from . import views

urlpatterns = [
    path('', views.open_backpack, name='open_backpack'),
    path('add/<item_id>', views.add_to_backpack, name='add_to_backpack'),
    
]