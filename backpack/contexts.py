def backpack_contents(request):
    backpack_items = []
    total = 0
    collectable_count = 0
    
    grand_total = total  # Assuming there's no additional delivery cost

    context = {
        'backpack_items': backpack_items,
        'total': total,
        'collectable_count': collectable_count,
        'grand_total': grand_total,
    }

    return context
