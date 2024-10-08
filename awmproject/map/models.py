from django.db import models
from django.contrib import admin

# Create your models here.
class(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.name
    
admin.site.register(Location)