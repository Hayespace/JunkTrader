from django.shortcuts import render, redirect

# Create your views here.

def open_backpack(request):
    

    return render(request, 'backpack/backpack.html')

def add_to_backpack(request, item_id):
    

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    backpack = request.session.get('backpack', {})

    if item_id in list(backpack.keys()):
        backpack[item_id] += quantity
    else:
        backpack[item_id] = quantity

    request.session['backpack'] = backpack
    print(request.session['backpack'])
    return redirect(redirect_url)
    