from django.contrib import admin
# import your models here
from .models import Dog, Walking, Treat

# Register your models here
admin.site.register(Dog)
admin.site.register(Walking)
admin.site.register(Treat)
