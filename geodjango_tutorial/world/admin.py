from django.contrib import admin

# Register your models here.
from .models import WorldBorder, Profile

admin.site.register(WorldBorder, admin.ModelAdmin)
admin.site.register(Profile, admin.ModelAdmin)