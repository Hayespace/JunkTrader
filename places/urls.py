from django.urls import path
from .views import update_collectable_prices, get_location_image
from .views import locations

urlpatterns = [
    path('update_collectable_prices/', update_collectable_prices, name='update_collectable_prices'),
    path('get_location_image/', get_location_image, name='get_location_image'),
    path('locations/', locations, name='locations'),
]
