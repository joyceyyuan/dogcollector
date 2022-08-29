from django.shortcuts import render
from django.http import HttpResponse

# Add the Dog class & list and view function below the imports
class Dog:  # Note that parens are optional if not inheriting from another class
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

dogs = [
    Dog('Rudy', 'Shiba Inu', 'a naughty dog loves to play', 2),
    Dog('Rolo', 'Labrador Retriever', 'a white Labrador Retriever', 0),
    Dog('Didi', 'Teddy', 'likes to interact with humans', 5)
]

# Define the home view
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
# Define the about view
def about(request):
    return render(request, 'about.html')
# Define the index view
def dogs_index(request):
    return render(request, 'dogs/index.html', { 'dogs': dogs })
