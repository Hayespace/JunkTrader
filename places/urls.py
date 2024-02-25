# places/urls.py

from django.urls import path
from .views import update_collectable_prices  # Import the view function

urlpatterns = [
    path('update_collectable_prices/', update_collectable_prices, name='update_collectable_prices'),
]
