from django.db import models
from django.contrib.auth.models import User


# Actual Plant Details
class PlantInfo(models.Model):
    common_name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    sun_needs = models.CharField(max_length=20, default='Full sun')
    water_frequency_days = models.IntegerField(default=2)
    days_to_harvest = models.IntegerField(default=60)

    def __str__(self):
        return self.common_name


class Garden(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Plant(models.Model):
    name = models.CharField(max_length=100)
    planted_date = models.DateField()
    last_watered = models.DateField(null=True, blank=True)
    notes = models.TextField(max_length=500, blank=True)
    garden = models.ForeignKey(Garden, on_delete=models.CASCADE)
    plant_info = models.ForeignKey(PlantInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
