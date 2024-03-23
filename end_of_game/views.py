from django import forms
from django.shortcuts import render, redirect


def end_of_game(request):
    print("In end of game")
    final_score = request.session.get('player_funds', 0)
    request.session.clear()
    return render(request, 'end_of_game/end_of_game.html', {'final_score': final_score})


'''
def submit_score(request):
    if request.method == 'POST':
        form = ScoreSubmissionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            score = form.cleaned_data['score']
            PlayerScore.objects.create(username=username, score=score)
            return redirect('home')
    else:
        form = ScoreSubmissionForm()
    return render(request, 'end_of_game/end_of_game.html', {'form': form})
'''