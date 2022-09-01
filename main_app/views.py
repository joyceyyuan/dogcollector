from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Dog
from django.http import HttpResponse


# Define the home view
def home(request):
    return render(request, 'home.html')
# Define the about view
def about(request):
    return render(request, 'about.html')
# Define the index view
def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})
# Define the detail view
def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id = dog_id)
    return render(request, 'dogs/detail.html', {'dog': dog})

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'
