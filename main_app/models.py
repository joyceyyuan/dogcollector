from django.db import models
# Import the reverse function
from django.urls import reverse

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    #this function will get called on a create or update on a Class Based View in order redirect the user
    def get_absolute_url(self):
        # detail is referring to the name of the route
        # path('dogs/<int:dog_id>/', views.dogs_detail, name="detail"),
        return reverse('detail', kwargs={'dog_id': self.id})
