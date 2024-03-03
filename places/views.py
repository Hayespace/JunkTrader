# views.py

import random
from django.shortcuts import render
from django.http import JsonResponse
from .models import Location

def update_collectable_prices(request):
    location_id = request.GET.get('location_id')
    if location_id is not None:
        # Retrieve the location object
        try:
            location = Location.objects.get(pk=location_id)
        except Location.DoesNotExist:
            return JsonResponse({'error': 'Location not found'}, status=404)

        # Update prices randomly
        collectables = location.collectable_set.all()
        for collectable in collectables:
            collectable.price = random.randint(50, 10000)
            collectable.save()

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'Location ID not provided'}, status=400)

# views.py

def locations(request):
    # Retrieve all locations from the database
    locations = Location.objects.all()
    print(locations)  # Add this line for debugging
    return render(request, 'fixed_panel.html', {'locations': locations})
