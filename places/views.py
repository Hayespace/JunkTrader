import random
from django.shortcuts import redirect
from collectables.models import Collectable
from django.http import JsonResponse
from .models import Location

def update_collectable_prices(request):
    # Retrieve all collectables
    collectables = Collectable.objects.all()
    
    # Update prices randomly
    for collectable in collectables:
        collectable.price = random.randint(50, 10000)
        collectable.save()
    

def get_location_image(request):
    location_id = request.GET.get('location_id')
    try:
        location = Location.objects.get(pk=location_id)
        image_url = location.picture.url
        return JsonResponse({'image_url': image_url})
    except Location.DoesNotExist:
        return JsonResponse({'error': 'Location not found'}, status=404)

def locations(request):
    # Retrieve all locations from the database
    locations = Location.objects.all()
    return render(request, 'fixed_panel.html', {'locations': locations})