from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Garden
from .forms import GardenForm

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
    if request.method == 'POST':
        garden.delete()
        return redirect('gardens-index')
    return render(request, 'gardens/confirm_delete.html', {'garden': garden})


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