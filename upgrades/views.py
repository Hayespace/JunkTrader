from django.shortcuts import render, get_object_or_404
from .models import Upgrade

def all_upgrades(request):
    upgrades = Upgrade.objects.all()
    context = {'upgrades': upgrades}
    return render(request, 'upgrades/all_upgrades.html', context)

def upgrade_detail(request, upgrade_id):
    upgrade = get_object_or_404(Upgrade, pk=upgrade_id)
    return render(request, 'upgrades/upgrade_detail.html', {'upgrade': upgrade})