from django.shortcuts import render, redirect

def index(request):
    if request.method == 'POST':
        # Check if the form is submitted
        # Initialize player's funds with $10,000
        request.session['player_funds'] = 10000
        # Redirect to the collectables page
        return redirect('collectables')
    else:
        return render(request, 'home/index.html')
