from django.db import models
from main_app.models import Church, Person

# Create your models here.

class Wedding(models.Model):
    date = models.DateField()
    time = models.TimeField()
    church = models.ForeignKey(Church, on_delete=models.CASCADE, related_name='wedding_church')
    minister = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='minister', default=1)

    def __str__(self):
        return str(self.date)
