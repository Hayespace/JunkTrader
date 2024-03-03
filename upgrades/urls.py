from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_upgrades, name='all_upgrades'),
    path('<int:upgrade_id>/', views.upgrade_detail, name='upgrade_detail'),
]
