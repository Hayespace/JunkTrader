import random
from collectables.models import Collectable

def update_collectable_prices(request):
    # Retrieve all collectables
    collectables = Collectable.objects.all()
    
    # Update prices randomly
    for collectable in collectables:
        collectable.price = random.randint(50, 10000)
        collectable.save()
    
    return redirect('collectables') 
