from django.shortcuts import render, redirect

def index(request):
    if request.method == 'POST':
        difficulty = request.POST.get('difficulty')
        if difficulty == 'easy':
            request.session['player_funds'] = 20000
        elif difficulty == 'medium':
            request.session['player_funds'] = 10000
        elif difficulty == 'difficult':
            request.session['player_funds'] = 5000
        return redirect('collectables')
    else:
        return render(request, 'home/index.html')

def reset_session(request):
    # Clear backpack items
    request.session['backpack'] = {}
    # Reset player funds
    request.session['player_funds'] = 0
    return redirect('home')