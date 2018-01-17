from django.db import models
from main_app.models import Church, Person

# Create your models here.


class ServiceType(models.Model):
    service_type = models.CharField(max_length=20)

    def __str__(self):
        return str(self.service_type)


class ServiceStatus(models.Model):
    service_status = models.CharField(max_length=20)

    def __str__(self):
        return str(self.service_status)

    class Meta:
        verbose_name_plural = "Service Statuses"


class Wedding(models.Model):
    date = models.DateField()
    time = models.TimeField()
    church = models.ForeignKey(Church, on_delete=models.CASCADE, related_name='wedding_church')
    minister = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='minister', default=1)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='type', default=1)
    service_status = models.ForeignKey(ServiceStatus, on_delete=models.CASCADE, related_name='status', default=1)
    dear = models.CharField(max_length=20)
    mail_title = models.CharField(max_length=30)
    banns_date = models.DateField()
    by_license = models.BooleanField(default=False)
    organ = models.BooleanField(default=False)
    choir = models.BooleanField(default=False)
    bells = models.BooleanField(default=False)
    flowers = models.BooleanField(default=False)
    video = models.BooleanField(default=False)
    cd = models.BooleanField(default=False)
    winter_heating = models.BooleanField(default=False)
    verger = models.BooleanField(default=False)
    car_park_attendant = models.BooleanField(default=False)
    marches = models.CharField(max_length=50, null=True, blank=True)
    singing = models.CharField(max_length=50, null=True, blank=True)
    organist = models.CharField(max_length=50, null=True, blank=True)
    order_of_service = models.BooleanField(default=False)
    office_to_print = models.BooleanField(default=False)
    flowers_details = models.CharField(max_length=100, null=True, blank=True)
    flowers_contact = models.CharField(max_length=100, null=True, blank=True)
    no_of_guests = models.IntegerField(default=0)
    wheelchair_access = models.CharField(max_length=50, null=True, blank=True)
    rehearsal_date = models.DateField(null=True, blank=True)
    rehearsal_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return str(self.date)


class ServiceReadings(models.Model):
    bible = models.CharField(max_length=50,null=True, blank=True)
    other = models.CharField(max_length=50,null=True, blank=True)
    reader = models.CharField(max_length=50)
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE, related_name="wedding_reading")

    def __str__(self):
        return str(self.reader)


class ServiceHymns(models.Model):
    hymn = models.CharField(max_length=50)
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE, related_name="wedding_hymn")

    def __str__(self):
        return str(self.hymn)