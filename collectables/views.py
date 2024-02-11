from django.shortcuts import render
from .models import Collectable

def all_collectables(request):

    collectables = Collectable.objects.all()

    context = {
        'collectables': collectables,
    }

    return render(request, 'collectables/collectables.html', context)
