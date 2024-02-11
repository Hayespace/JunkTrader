from django.shortcuts import render, get_object_or_404
from .models import Collectable

def all_collectables(request):

    collectables = Collectable.objects.all()

    context = {
        'collectables': collectables,
    }

    return render(request, 'collectables/collectables.html', context)


def collectable_detail(request, collectable_id):

    collectable = get_object_or_404(Collectable, pk=collectable_id)

    context = {
        'collectable': collectable,
    }

    return render(request, 'collectables/collectable_detail.html', context)
