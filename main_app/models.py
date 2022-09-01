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

# Set up Field Choices
SCHEDULE = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night'),
)

class Walking(models.Model):
    # the first optional positional argument overrides the label
    date = models.DateField('walking date')
    schedule = models.CharField(
        'walking schedule',
        max_length=1, 
        choices=SCHEDULE,  
        default=SCHEDULE[0][0]  # 'M'
    )

    # create the dog_id FK (Foriegn Key)
    # on_Delete is saying if we delete a dog, delete all of the walkings the dog has, so no walkings exist without a dog
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        # obtaining the human readable value of a Field.choice ('Morning')
        return f"{self.get_schedule_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
