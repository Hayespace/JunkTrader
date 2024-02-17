from django.shortcuts import get_object_or_404
from collectables.models import Collectable

def backpack_contents(request):
    backpack_items = []
    total = 0
    collectable_count = 0
    backpack = request.session.get('backpack', {})

    for item_id, quantity in backpack.items():
        collectable = get_object_or_404(Collectable, pk=item_id)
        total += quantity * collectable.price
        collectable_count += quantity
        backpack_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'collectable': collectable,
        })
    
    grand_total = total  # Assuming there's no additional delivery cost

    context = {
        'backpack_items': backpack_items,
        'total': total,
        'collectable_count': collectable_count,
        'grand_total': grand_total,
    }

    return context
