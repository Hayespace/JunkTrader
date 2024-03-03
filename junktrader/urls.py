from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import reset_session  # Import the reset_session view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('collectables/', include('collectables.urls')),
    path('backpack/', include('backpack.urls')),
    path('places/', include('places.urls')),
    path('upgrades/', include('upgrades.urls')),
    path('reset-session/', reset_session, name='reset_session'),  # Add the URL pattern for reset_session
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
