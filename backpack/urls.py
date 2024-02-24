from django.urls import path
from . import views

urlpatterns = [
    path('', views.open_backpack, name='open_backpack'),
    path('adjust/<item_id>/', views.adjust_backpack, name='adjust_backpack'),
]
