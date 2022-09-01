from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog
from .forms import WalkingForm
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
    # instantiate WalkingForm to be rendered in the template
    walking_form = WalkingForm()
    return render(request, 'dogs/detail.html', {'dog': dog, 'walking_form': walking_form})

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'

class DogUpdate(UpdateView):
    model = Dog 
    # exclude the name from update  
    fields = ['breed', 'description', 'age'] 

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/' # if we delete a dog, we'll need to redirect to the dogs index page since that dog doesn't exist anymore.,

def add_walking(request, dog_id):
    # we need to create a modelForm instance using the data from request.POST
    form = WalkingForm(request.POST)
    # validate the form, so make sure the inputs are of the correct type and shape
    if form.is_valid():
        # were creating an object to save to the database, but don't save yet, because
        # we need to add dog_id
        new_walking = form.save(commit=False)
        new_walking.dog_id = dog_id
        new_walking.save()  # saves the walking to the database!
    # import redirect at the top
    return redirect('detail', dog_id=dog_id) #can be shorten as redirect('detail', dog_id)