from django.shortcuts import render, redirect

def open_backpack(request):
    """A view that renders the backpack contents page"""
    return render(request, 'backpack/backpack.html')

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
        if item_id in backpack:
            backpack[item_id] += quantity
        else:
            backpack[item_id] = quantity
    else:
        # Decrease the quantity of the item in the backpack
        if item_id in backpack:
            backpack[item_id] -= abs(quantity)
            if backpack[item_id] <= 0:
                del backpack[item_id]

    # Update the session with the modified backpack
    request.session['backpack'] = backpack

    # Redirect to the specified URL
    return redirect(redirect_url)


