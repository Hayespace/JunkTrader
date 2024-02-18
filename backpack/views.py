from django.shortcuts import render, redirect, reverse

# Create your views here.

def open_backpack(request):
    """ A view that renders the backpack contents page """

    return render(request, 'backpack/backpack.html')

def add_to_backpack(request, item_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # Get backpack from session or initialize it as an empty dictionary
    backpack = request.session.get('backpack', {})

    if item_id in backpack:
        backpack[item_id] += quantity
    else:
        backpack[item_id] = quantity

    request.session['backpack'] = backpack
    return redirect(redirect_url)


def adjust_backpack(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    backpack = request.session.get('backpack', {})

    if quantity > 0:
        backpack[item_id] = quantity
    else:
        backpack.pop(item_id, None)

    request.session['backpack'] = backpack
    return redirect(reverse('open_backpack'))



