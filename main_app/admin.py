from django.contrib import admin
from .models import Person
# Register your models here.
from .models import Church
from .models import Person

admin.site.register(Person)
admin.site.register(Church)