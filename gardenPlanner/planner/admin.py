from django.contrib import admin
from .models import Garden, Plant, PlantInfo

admin.site.register(Garden)
admin.site.register(Plant)
admin.site.register(PlantInfo)
