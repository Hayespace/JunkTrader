# places/models.py

from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to='locations')

    def __str__(self):
        return self.name
