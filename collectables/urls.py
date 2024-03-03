from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_collectables, name='collectables'),
    path('<int:collectable_id>/', views.collectable_detail, name='collectable_detail'),
    path('update_prices/', views.update_collectable_prices, name='update_collectable_prices'),
    path('add/<int:item_id>/', views.add_to_backpack, name='add_to_backpack'),
    path('sell/<int:collectable_id>/', views.sell_item, name='sell_item'),
]