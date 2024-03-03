from django.shortcuts import render, redirect
from django.http import JsonResponse

def open_backpack(request):
    """A view that renders the backpack contents page"""
    return render(request, 'backpack/backpack.html')

from django.shortcuts import redirect

def adjust_backpack(request, item_id):
    """Adjust the quantity of an item in the backpack"""

    quantity_str = request.POST.get('quantity')
    if not quantity_str:
        # Redirect to the previous page with an error message if quantity is not provided
        return redirect('open_backpack') 

    try:
        quantity = int(quantity_str)
    except ValueError:
        # Redirect to the previous page with an error message if quantity is not a valid integer
        return redirect('open_backpack')  

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

    return redirect(redirect_url)



def sell_item(request, item_id):
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
    print(f'backpack: {backpack}')
    print(f'type(item_id): {type(item_id)}')
    if quantity_to_sell > 0:
        print('quantity > 0')
        
        item_id_str = str(item_id)
        print(f'item_id_str: {item_id_str}')
        # Check if the item exists in the backpack
        if item_id_str in backpack:
            print('in backpack')
            # Ensure the quantity to sell is not greater than the quantity in the backpack
            if quantity_to_sell <= backpack[item_id_str]:
                # Subtract the quantity to sell from the quantity in the backpack
                backpack[item_id_str] -= quantity_to_sell
                # If the remaining quantity is zero or negative, remove the item from the backpack
                if backpack[item_id_str] <= 0:
                    del backpack[item_id_str]
        else:
            # Handle the case where the item is not in the backpack
            print('not in backpack')
            pass

    # Update the session with the modified backpack
    request.session['backpack'] = backpack

    # Redirect to the specified URL
    return redirect(redirect_url)





    
        

