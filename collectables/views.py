from django.shortcuts import render, get_object_or_404, redirect
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

def add_to_backpack(request, item_id):
    """Adjust the quantity of an item in the backpack"""

    quantity_str = request.POST.get('quantity')
    if quantity_str is None:
        # Redirect to the previous page with an error message if quantity is not provided
        return redirect('collectable_detail', collectable_id=item_id)

    quantity = int(quantity_str)
    redirect_url = request.POST.get('redirect_url', '/backpack/') 

    # Get backpack from session or initialize it as an empty dictionary
    backpack = request.session.get('backpack', {})

    if quantity > 0:
        # Update the quantity of the item in the backpack
        if item_id in backpack:
            backpack[item_id] += quantity
        else:
            backpack[item_id] = quantity

    # Update the session with the modified backpack
    request.session['backpack'] = backpack

    # Redirect to the specified URL
    return redirect(redirect_url)

def sell_item(request, item_id):
    quantity_str = request.POST.get('quantity')
    if quantity_str is None:
        return redirect('collectable_detail', collectable_id=item_id)

    quantity = int(quantity_str)

    # Get backpack from session or initialize it as an empty dictionary
    backpack = request.session.get('backpack', {})

    if quantity > 0:
        # Check if the item exists in the backpack
        if item_id in backpack:
            # Reduce the quantity of the item in the backpack
            backpack[item_id] -= quantity
            if backpack[item_id] <= 0:
                del backpack[item_id]  # Remove the item if the quantity becomes zero or negative
        else:
            # Handle the case where the item is not in the backpack
            # You may want to add some error handling or redirection here
            pass

    # Update the session with the modified backpack
    request.session['backpack'] = backpack

    # Redirect to the collectable detail page
    return redirect('collectable_detail', collectable_id=item_id)
