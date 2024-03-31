from django.shortcuts import render, get_object_or_404
from .models import UserProfile

def profile(request):
    """ Display the user's profile and top scores. """
    # Get the user's profile
    profile = get_object_or_404(UserProfile, user=request.user)
    
    # Get scores for the logged-in user
    user_scores = UserProfile.objects.filter(user=request.user)

    # Get all user profiles for the top scores
    top_scores = UserProfile.objects.all()

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'user_scores': user_scores,
        'top_scores': top_scores,
    }

    return render(request, template, context)


def list_scores():
    """ Retrieve and return the list of scores for all users. """
    all_user_profiles = UserProfile.objects.all()
    return all_user_profiles


