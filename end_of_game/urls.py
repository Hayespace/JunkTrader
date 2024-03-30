from django.urls import path
from . import views

urlpatterns = [
    path('', views.end_of_game, name='end_of_game'),
    path('submit_score/', views.submit_score, name='submit_score'),
]

