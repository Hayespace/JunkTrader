# urls.py
from django.urls import path
from . import views
from .views import purchase_upgrade

urlpatterns = [
    path('upgrades/', views.all_upgrades, name='all_upgrades'),
    path('purchase_upgrade/<int:upgrade_id>/', views.purchase_upgrade, name='purchase_upgrade'),
]

