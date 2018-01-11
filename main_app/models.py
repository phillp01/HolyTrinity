from django.db import models
from django.utils.text import slugify
# Create your models here.

class Church(models.Model):
    church_name = models.CharField(max_length=50)

    def __str__(self):
        return self.church_name

    class Meta:
        verbose_name_plural = "Churches"

class Person(models.Model):
    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True)
    email = models.EmailField(max_length=100)
    church = models.ForeignKey(Church, on_delete=models.CASCADE, related_name='church')

    class Meta:
        verbose_name_plural = "People"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.first_name + ' ' + self.last_name)
        super(Person, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


