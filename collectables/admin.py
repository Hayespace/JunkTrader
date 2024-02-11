from django.contrib import admin
from .models import Collectable

# Register your models here.

class CollectableAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'image',
    )

    ordering = ('name',)

admin.site.register(Collectable, CollectableAdmin)