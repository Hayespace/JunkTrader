# views.py
from django.shortcuts import render, redirect
from .models import Upgrade
import stripe

def all_upgrades(request):
    upgrades = Upgrade.objects.all()
    context = {'upgrades': upgrades}
    return render(request, 'upgrades/all_upgrades.html', context)

def purchase_upgrade(request, upgrade_id):
    # Retrieve the upgrade object based on the upgrade_id
    upgrade = Upgrade.objects.get(pk=upgrade_id)

    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # Create a Stripe Checkout Session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': upgrade.name,
                    },
                    'unit_amount': int(upgrade.price * 100),  # Stripe requires the amount in cents
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('open_backpack')),  # Redirect to the backpack page after successful payment
            cancel_url=request.build_absolute_uri(reverse('cancel_upgrade')),  # Redirect to a cancel page if payment is cancelled
        )

        return redirect(session.url)

    # Update session data with the new capacity
    request.session['backpack_capacity'] = upgrade.capacity
    return redirect('open_backpack')
