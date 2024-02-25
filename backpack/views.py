from django.shortcuts import render, redirect
from django.http import JsonResponse

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

        return redirect('open_backpack')

    quantity = int(quantity_str)
    redirect_url = request.POST.get('redirect_url', '/backpack/') 

    
    backpack = request.session.get('backpack', {})

    if quantity > 0:
        
        if item_id in backpack:
            backpack[item_id] - quantity
        else:
            backpack[item_id] = quantity

    # Update the session with the modified backpack
    request.session['backpack'] = backpack

    # Redirect to the specified URL
    return redirect(redirect_url)
    
        

