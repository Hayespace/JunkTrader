from django.shortcuts import render, redirect
from profiles.models import UserProfile
from django.contrib.auth.decorators import login_required
from datetime import datetime


def end_of_game(request):
    print("In end of game")
    final_score = request.session.get('player_funds', 0)
    return render(request, 'end_of_game/end_of_game.html', {'final_score': final_score})

@login_required
def submit_score(request):
    if request.method == 'POST':
        submitted_score = request.POST.get('score')
        
        try:
            score_int = int(float(submitted_score))
        except ValueError:
            print("Invalid score format")
            return redirect('error_page')  

        # Check if the user already has a profile
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        
        # If the profile already exists, update the score and date
        if not created:
            profile.scores = score_int
            profile.date = datetime.now()
        else:
            profile.scores += score_int
            profile.date = datetime.now()
        
        profile.save()
        
        print("Score submitted successfully.")
        return redirect('profile')
    else:
        return redirect('error_page')

