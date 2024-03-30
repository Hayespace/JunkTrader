from django.shortcuts import render, redirect

def end_of_game(request):
    print("In end of game")
    final_score = request.session.get('player_funds', 0)
    return render(request, 'end_of_game/end_of_game.html', {'final_score': final_score})
