from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Garden, Plant
from .forms import GardenForm, PlantForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


@login_required
def gardens_index(request):
    gardens = Garden.objects.filter(user=request.user)
    return render(request, 'gardens/index.html', {'gardens': gardens})


@login_required
def gardens_detail(request, garden_id):
    garden = get_object_or_404(Garden, pk=garden_id, user=request.user)
    return render(request, 'gardens/detail.html', {'garden': garden})


@login_required
def gardens_create(request):
    if request.method == 'POST':
        form = GardenForm(request.POST)
        if form.is_valid():
            garden = form.save(commit=False)
            garden.user = request.user
            garden.save()
            return redirect('gardens-detail', garden_id=garden.id)
    else:
        form = GardenForm()
    return render(request, 'gardens/form.html', {'form': form})


@login_required
def gardens_delete(request, garden_id):
    garden = get_object_or_404(Garden, pk=garden_id, user=request.user)
    garden.delete()
    return redirect('gardens-index')


@login_required
def plants_create(request, garden_id):
    garden = get_object_or_404(Garden, pk=garden_id, user=request.user)
    if request.method == 'POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            plant = form.save(commit=False)
            plant.garden = garden
            plant.save()
            return redirect('plants-detail', plant_id=plant.id)
    else:
        form = PlantForm()
    return render(request, 'plants/form.html', {'form': form, 'garden': garden})


@login_required
def plants_detail(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id, garden__user=request.user)
    return render(request, 'plants/detail.html', {'plant': plant})


@login_required
def plants_delete(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id, garden__user=request.user)
    garden_id = plant.garden.id
    plant.delete()
    return redirect('gardens-detail', garden_id=garden_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)