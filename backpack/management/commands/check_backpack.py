from django.core.management.base import BaseCommand
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore

class Command(BaseCommand):
    help = 'Check the quantity of items in the backpack'

    def handle(self, *args, **kwargs):
        sessions = Session.objects.all()
        for session in sessions:
            data = SessionStore(session_key=session.session_key)
            if 'backpack' in data:
                backpack_data = data['backpack']
                print(f"Session Key: {session.session_key}")
                print("Backpack:")
                for item_id, quantity in backpack_data.items():
                    print(f"Item ID: {item_id}, Quantity: {quantity}")
            else:
                print(f"No backpack data found in session {session.session_key}")
