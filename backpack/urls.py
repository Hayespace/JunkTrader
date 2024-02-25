from django.urls import path
from . import views
from .views import sell_item

urlpatterns = [
    path('', views.open_backpack, name='open_backpack'),
    path('adjust/<item_id>/', views.adjust_backpack, name='adjust_backpack'),
    path('sell/<int:item_id>/', sell_item, name='sell_item'),
]
