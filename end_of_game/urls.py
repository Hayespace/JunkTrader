from django.urls import path
from . import views

urlpatterns = [
    path('', views.end_of_game, name='end_of_game'),
]

