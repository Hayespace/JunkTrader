from django.shortcuts import get_object_or_404
from collectables.models import Collectable

def backpack_contents(request):
    backpack_items = []
    total = 0
    total_quantity = 0
    collectable_count = 0
    backpack = request.session.get('backpack', {})

    for item_id, quantity in backpack.items():
        collectable = get_object_or_404(Collectable, pk=item_id)
        total += quantity * collectable.price
        total_quantity += quantity
        collectable_count += quantity
        backpack_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'collectable': collectable,
            'subtotal': quantity * collectable.price,  # Include subtotal for each item
            'quantity_in_backpack': quantity,  # Add quantity in backpack
            'total_value_in_backpack': quantity * collectable.price,  # Add total value in backpack
        })

    grand_total = total  

    context = {
        'backpack_items': backpack_items,
        'total': total,
        'total_quantity': total_quantity, 
        'collectable_count': collectable_count,
        'grand_total': grand_total,
    }

    return context

def total_amount(request):
    total_amount = 10000  
    return {'total_amount': total_amount}

