from django.shortcuts import render, redirect
from profiles.models import UserProfile
from datetime import datetime


def end_of_game(request):
    print("In end of game")
    final_score = request.session.get('player_funds', 0)
    return render(request, 'end_of_game/end_of_game.html', {'final_score': final_score})

def submit_score(request):
    if request.method == 'POST':
        submitted_score = request.POST.get('score')
        
        try:
            score_int = int(float(submitted_score))
        except ValueError:
            return redirect('error_page')  

        # Retrieve the user's profile
        profile = request.user.userprofile
        
        # Update the user's profile with the new score and current date
        profile.scores += score_int
        profile.date = datetime.now().date()  # Update the date field with the current date
        profile.save()
        
        return redirect('profile')
    else:
        return redirect('error_page')

