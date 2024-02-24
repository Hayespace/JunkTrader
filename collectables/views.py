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

def adjust_backpack(request, item_id):
    """Adjust the quantity of an item in the backpack"""

    quantity_str = request.POST.get('quantity')
    if quantity_str is None:
        # Redirect to the previous page with an error message if quantity is not provided
        return redirect('open_backpack')  # Adjust the URL name as needed

    quantity = int(quantity_str)
    redirect_url = request.POST.get('redirect_url', '/backpack/')  # Default to backpack page if redirect_url is None

    # Get backpack from session or initialize it as an empty dictionary
    backpack = request.session.get('backpack', {})

    if quantity > 0:
        # Update the quantity of the item in the backpack
        backpack[item_id] = quantity
    else:
        # Remove the item from the backpack if quantity is zero or less
        backpack.pop(item_id, None)

    # Update the session with the modified backpack
    request.session['backpack'] = backpack

    # Redirect to the specified URL
    return redirect(redirect_url)