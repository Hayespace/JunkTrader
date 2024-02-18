from django.contrib import admin
from .models import Collectable

class CollectableAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'image',
        'glb_file',
    )

    ordering = ('id',)

admin.site.register(Collectable, CollectableAdmin)
