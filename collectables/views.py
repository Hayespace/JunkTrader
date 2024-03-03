# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.cache import never_cache
from .models import Collectable
import random

@never_cache
def update_collectable_prices(request):
    try:
        collectables = Collectable.objects.all()
        for collectable in collectables:
            collectable.price = random.randint(50, 10000)
            collectable.save()
        response_data = {'success': True}
        response = JsonResponse(response_data)
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

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
    quantity_str = request.POST.get('quantity')
    if not quantity_str:
        return redirect('collectable_detail', collectable_id=item_id)

    try:
        quantity = int(quantity_str)
    except ValueError:
        return redirect('collectable_detail', collectable_id=item_id)

    redirect_url = request.POST.get('redirect_url', '/backpack/') 

    backpack = request.session.get('backpack', {})

    if quantity > 0:
        if item_id in backpack:
            backpack[item_id] += quantity
        else:
            backpack[item_id] = quantity

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
