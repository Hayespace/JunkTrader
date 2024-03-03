from django.urls import path
from .views import update_collectable_prices

urlpatterns = [
    path('update_prices/', update_collectable_prices, name='update_collectable_prices'),
    
]
