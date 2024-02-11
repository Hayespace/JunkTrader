from django.urls import path
from . import views

urlpatterns = [
    path('', views.open_backpack, name='open_backpack')
    
]