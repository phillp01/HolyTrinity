from django.db import models
from main_app.models import Church, Person, Ministers
from decimal import Decimal
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
    bride = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='bride_name')
    groom = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='groom_name')
    date = models.DateField()
    time = models.TimeField()
    church = models.ForeignKey(Church, on_delete=models.CASCADE, related_name='wedding_church')
    minister = models.ForeignKey(Ministers, on_delete=models.CASCADE, related_name='minister', default=1)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='type', default=1)
    service_status = models.ForeignKey(ServiceStatus, on_delete=models.CASCADE, related_name='status', default=1)
    dear = models.CharField(max_length=20)
    mail_title = models.CharField(max_length=30)
    banns_date = models.DateField()
    bible = models.CharField(max_length=20,null=True, blank=True)
    reader = models.CharField(max_length=20,null=True, blank=True,verbose_name='Bible Reader')
    other = models.CharField(max_length=20,null=True, blank=True)
    other_reader = models.CharField(max_length=50, null=True, blank=True,verbose_name='Other Reader')
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
    Hymn1 = models.CharField(max_length=50, null=True, blank=True)
    Hymn2 = models.CharField(max_length=50, null=True, blank=True)
    Hymn3 = models.CharField(max_length=50, null=True, blank=True)
    Hymn4 = models.CharField(max_length=50, null=True, blank=True)
    Hymn5 = models.CharField(max_length=50, null=True, blank=True)
    Hymn6 = models.CharField(max_length=50, null=True, blank=True)
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
    total_paid = models.CharField(max_length=50, null=True, blank=True)
    date_amount_paid = models.TextField(null=True, blank=True,verbose_name='Dates and Amounts Paid')
    notes = models.TextField(null=True, blank=True)
    first_visit = models.CharField(max_length=50, null=True, blank=True)
    second_visit = models.CharField(max_length=50, null=True, blank=True)
    third_visit = models.CharField(max_length=50, null=True, blank=True)
    evidence_filed = models.BooleanField(default=False,verbose_name='Evidence Filed')
    decree_abs_seen = models.BooleanField(default=False,verbose_name='Decree Abs Seen')
    banns_no = models.CharField(max_length=50, null=True, blank=True)

    
    def __str__(self):
        return str(self.id)

# class ChurchPrice(models.Model):
	# price = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))	
	# church = models.ForeignKey(Church, on_delete=models.CASCADE, related_name='churchId')
	# fromDate = models.DateField(null=True, blank=True)
	# toDate = models.DateField(null=True, blank=True)

class additionalServices(models.Model):
	
	Additional_services_choices = (
        ('By License', 'By License'),
        ('Organ', 'Organ'),
        ('Choir', 'Choir'),
        ('Bells', 'Bells'),
        ('Flowers', 'Flowers'),
        ('Video', 'Video'),
        ('Cd', 'Cd'),
        ('Winter Heating', 'Winter Heating'),
        ('Verger', 'Verger'),
        ('Car Park Attendant', 'Car Park Attendant'),
     
    )
	name = models.CharField(
        max_length=100,
        choices=Additional_services_choices,
        blank=False,
        verbose_name='Additional Services',
        default=Decimal('0.0000')
    )
	current_price = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'),)
	upcoming_price = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'),)
	upcoming_date = models.DateField(null=True, blank=True)	



class ServiceReading(models.Model):
    bible = models.CharField(max_length=50, null=True, blank=True)
    other = models.CharField(max_length=50, null=True, blank=True)
    reader = models.CharField(max_length=50)
    other_reader = models.CharField(max_length=50, null=True, blank=True)
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE, related_name="wedding_reading")

    def __str__(self):
        return str(self.reader)


class ServiceHymn(models.Model):
    hymn = models.CharField(max_length=50)
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE, related_name="wedding_hymn")

    def __str__(self):
        return str(self.hymn)