from django.db import models

class Upgrade(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    glb_file = models.FileField(upload_to='glb_files/', null=True, blank=True)
    capacity = models.IntegerField(default=50)

    def __str__(self):
        return self.name

