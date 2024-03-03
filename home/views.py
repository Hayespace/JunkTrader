# home/views.py
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
        
        # Set default backpack capacity to 50
        request.session['backpack_capacity'] = 50

        # Initialize days played to 1
        request.session['days_played'] = 1
        
        return redirect('collectables')
    else:
        # Get the days played count from session data
        days_played = request.session.get('days_played', 0)
        return render(request, 'home/index.html', {'days_played': days_played})


def reset_session(request):
    # Clear backpack items
    request.session['backpack'] = {}
    # Reset player funds
    request.session['player_funds'] = 0
    # Reset days played
    request.session['days_played'] = 0
    return redirect('home')
