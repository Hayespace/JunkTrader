from django.shortcuts import render, redirect

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


