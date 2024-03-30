from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import JsonResponse
from .models import Collectable
from django.contrib import messages
from decimal import Decimal
import random


def increment_days_played(request):
    try:
        # Get the current days played count from the session
        days_played = request.session.get('days_played', 0)
        
        # Increment the days played count by 1
        days_played += 1

        # Limit the days played count to a maximum of 30
        days_played = min(days_played, 30)

        print("Days played:", days_played)  

        # Display special messages at certain days
        if days_played == 25:
            messages.warning(request, "You have 5 days of trading left.")
        elif days_played == 29:
            messages.warning(request, "This is your last day of trading. Make it count!")
        elif days_played > 29:
            print("Redirecting to end of game...") 
            # Redirect to the end of the game view
            return redirect(reverse('end_of_game'))
        
        # Update the days played count in the session
        request.session['days_played'] = days_played
        
        # Return a success response
        return JsonResponse({'success': True})
    except Exception as e:
        # Return an error response if an exception occurs
        return JsonResponse({'error': str(e)}, status=500)

def update_collectable_prices(request):
    try:
        collectables = Collectable.objects.all()
        for collectable in collectables:
            # Generate a new random price
            new_price = random.randint(50, 10000)
            # Store the previous price
            collectable.previous_price = collectable.price
            
            # Update the price of the collectable
            collectable.price = new_price
            collectable.save()

        # Pass the collectables to the template
        context = {'collectables': collectables}
        
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
    
    # Ensure 'player_funds' is set in the session with a default value if it's not found
    player_funds = request.session.get('player_funds', 0)

    # Get the total items currently in the backpack
    total_items_in_backpack = sum(backpack.values())
    
    # Get the capacity of the backpack from session
    backpack_capacity = request.session.get('backpack_capacity', 100)  

    # Get the price of the item
    item = get_object_or_404(Collectable, pk=item_id)
    item_price = item.price
    
    # Check if adding the item would exceed the backpack capacity
    if total_items_in_backpack + quantity > backpack_capacity:
        # Add an error message and redirect to the collectable detail page
        messages.error(request, "Adding this item would exceed the backpack capacity.")
        return redirect('collectable_detail', collectable_id=item_id)

    # Check if the player has enough funds
    total_cost = item_price * quantity
    if total_cost > Decimal(player_funds):
        messages.error(request, "You don't have enough funds to make this purchase.")
        return redirect('collectable_detail', collectable_id=item_id)

    if quantity > 0:
        if item_id in backpack:
            backpack[item_id] += quantity
        else:
            backpack[item_id] = quantity

        # Update player funds
        request.session['player_funds'] = str(Decimal(player_funds) - total_cost)
        
        # Add success message
        messages.success(request, "Item added to backpack successfully.")

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

    # Get backpack from session 
    backpack = request.session.get('backpack', {})
    
    if quantity_to_sell > 0:
        item_id_str = str(item_id)
        
        # Check if the item exists in the backpack
        if item_id_str in backpack:
            # Ensure the quantity to sell is not greater than the quantity in the backpack
            if quantity_to_sell <= backpack[item_id_str]:
                # Subtract the quantity to sell from the quantity in the backpack
                backpack[item_id_str] -= quantity_to_sell
                # If the remaining quantity is zero or negative, remove the item from the backpack
                if backpack[item_id_str] <= 0:
                    del backpack[item_id_str]
                
                # Update player funds
                item = get_object_or_404(Collectable, pk=item_id)
                print(f"Item price: {item.price}, Quantity to sell: {quantity_to_sell}")
                print(f"Current player funds: {request.session['player_funds']}")
                request.session['player_funds'] = str(Decimal(request.session['player_funds']) - (item.price * quantity_to_sell))
                print(f"Updated player funds: {request.session['player_funds']}")

    # Update the session with the modified backpack
    request.session['backpack'] = backpack

    # Redirect to the specified URL
    return redirect(redirect_url)
