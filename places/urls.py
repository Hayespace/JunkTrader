# urls.py

from django.urls import path
from .views import update_collectable_prices, locations

urlpatterns = [
    path('update_collectable_prices/', update_collectable_prices, name='update_collectable_prices'),
    path('locations/', locations, name='locations'),
]
