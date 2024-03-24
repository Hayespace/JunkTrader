from django.http import JsonResponse
from django.views.decorators.cache import never_cache 
from collectables.models import Collectable
import random

@never_cache  # Apply never_cache decorator to the view
def update_collectable_prices(request):
    try:
        collectables = Collectable.objects.all()
        for collectable in collectables:
            collectable.price = random.randint(50, 10000)
            collectable.save()
        response_data = {'success': True}
        response = JsonResponse(response_data)
        # Add cache control headers to ensure the response is not cached
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
