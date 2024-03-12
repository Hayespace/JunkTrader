from django.urls import path
from . import views

urlpatterns = [
    path('upgrades/', views.all_upgrades, name='all_upgrades'),
    path('purchase_upgrade/<int:upgrade_id>/', views.purchase_upgrade, name='purchase_upgrade'),
    path('upgrades/upgrade_success/<int:upgrade_id>/', views.upgrade_success, name='upgrade_success'),  
]
