# views.py
from django.shortcuts import render, redirect
from .models import Upgrade

def all_upgrades(request):
    upgrades = Upgrade.objects.all()
    context = {'upgrades': upgrades}
    return render(request, 'upgrades/all_upgrades.html', context)

def purchase_upgrade(request, upgrade_id):
    upgrade = Upgrade.objects.get(pk=upgrade_id)
    # Update session data with the new capacity
    request.session['backpack_capacity'] = upgrade.capacity
    return redirect('open_backpack') 
