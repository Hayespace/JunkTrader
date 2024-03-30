from django.contrib import admin
from .models import UserProfile

# Register the UserProfile model with the admin site
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'scores']  # Display user and scores fields in the admin list
    search_fields = ['user__username']  # Enable searching by username
