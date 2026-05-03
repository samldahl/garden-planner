from django import forms
from .models import Garden, Plant


class GardenForm(forms.ModelForm):
    class Meta:
        model = Garden
        fields = ['name', 'description']


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'plant_info', 'planted_date', 'notes']
        widgets = {
            'planted_date': forms.DateInput(attrs={'type': 'date'}),
        }
