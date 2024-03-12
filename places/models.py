from django.db import models

class Collectable(models.Model):
    # Define the fields for the Collectable model
    name = models.CharField(max_length=100)
    # Add other fields as needed

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()  # Add description field
    picture = models.ImageField(upload_to='location_pictures/')  # Add picture field

    def __str__(self):
        return self.name