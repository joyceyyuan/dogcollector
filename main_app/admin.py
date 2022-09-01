from django.contrib import admin
# import your models here
from .models import Dog, Walking

# Register your models here
admin.site.register(Dog)
# register the new Walking Model 
admin.site.register(Walking)
