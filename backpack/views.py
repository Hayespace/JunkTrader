from django.shortcuts import render, redirect
from django.contrib import messages

def open_backpack(request):
    """A view that renders the backpack contents page"""
    return render(request, 'backpack/backpack.html')

def adjust_backpack(request, item_id):
    """Adjust the quantity of an item in the backpack"""
    quantity_str = request.POST.get('quantity')
    if not quantity_str:
        # Redirect to the previous page with an error message if quantity is not provided
        messages.error(request, "Quantity not provided.")
        return redirect('open_backpack')

    try:
        quantity = int(quantity_str)
    except ValueError:
        # Redirect to the previous page with an error message if quantity is not a valid integer
        messages.error(request, "Invalid quantity.")
        return redirect('open_backpack')

    redirect_url = request.POST.get('redirect_url', '/backpack/') 

    # Get backpack from session or initialize it as an empty dictionary
    backpack = request.session.get('backpack', {})
    total_items_in_backpack = sum(backpack.values())

    # Check if adding the item would exceed the backpack capacity
    if 'backpack_capacity' in request.session:
        backpack_capacity = request.session['backpack_capacity']
        if total_items_in_backpack + quantity > backpack_capacity:
            # Display an error message if adding the item would exceed the capacity
            messages.error(request, "Adding this item would exceed the backpack capacity.")
            return redirect('open_backpack')

    if quantity > 0:
        # Update the quantity of the item in the backpack
        if item_id in backpack:
            backpack[item_id] += quantity
        else:
            backpack[item_id] = quantity

    # Update the session with the modified backpack
    request.session['backpack'] = backpack

    return redirect(redirect_url)

def sell_item(request, item_id):
    """Sell an item from the backpack"""
    quantity_str = request.POST.get('quantity')
    if quantity_str is None:
        return redirect('open_backpack')

    try:
        quantity_to_sell = int(quantity_str)
    except ValueError:
        return redirect('open_backpack')

    redirect_url = request.POST.get('redirect_url', '/backpack/') 

    # Get backpack from session or initialize it as an empty dictionary
    backpack = request.session.get('backpack', {})
    
    # Check if the item exists in the backpack
    if str(item_id) in backpack:
        # Ensure the quantity to sell is not greater than the quantity in the backpack
        if quantity_to_sell <= backpack[str(item_id)]:
            # Subtract the quantity to sell from the quantity in the backpack
            backpack[str(item_id)] -= quantity_to_sell
            # If the remaining quantity is zero or negative, remove the item from the backpack
            if backpack[str(item_id)] <= 0:
                del backpack[str(item_id)]
        else:
            # Display an error message if trying to sell more than available in the backpack
            messages.error(request, "Quantity to sell exceeds available quantity in backpack.")
    else:
        # Display an error message if the item is not in the backpack
        messages.error(request, "Item not found in backpack.")

    # Update the session with the modified backpack
    request.session['backpack'] = backpack

    # Redirect to the specified URL
    return redirect(redirect_url)
