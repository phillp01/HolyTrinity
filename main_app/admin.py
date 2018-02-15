from django.contrib import admin
from .models import Person
# Register your models here.
from .models import Church, qualifyingConnections, Proofs, Person, Ministers

admin.site.register(Person)
admin.site.register(Church)
admin.site.register(qualifyingConnections)
admin.site.register(Proofs)
admin.site.register(Ministers)