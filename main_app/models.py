from django.db import models
from django.utils.text import slugify
# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.first_name + ' ' + self.last_name)
        super(Person, self).save(*args, **kwargs)


    def __str__(self):
        return self.first_name + ' ' + self.last_name