from django.db import models

class Collectable(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    previous_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    glb_file = models.FileField(upload_to='glb_files/', null=True, blank=True)

    def __str__(self):
        return self.name
