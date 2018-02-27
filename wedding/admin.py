from django.contrib import admin
#from .models import Wedding, ServiceStatus, ServiceType,additionalServices
from .models import Wedding, ServiceStatus, ServiceType
from .forms import WeddingForm
# Register your models here.


# class WeedingaddtionalList(admin.ModelAdmin):
	# list_display = ["name","current_price","upcoming_price","upcoming_date"]

class Weedingsform(admin.ModelAdmin):
	list_display = ["mail_title","church","minister","date"]		
	#list_filter  = ["mail_title","church","minister","date"]		
	#form = WeddingForm		
	fields = [
            ('date',
            'time'),
            ('bride',
            'groom'),
            ('church',
            'minister'),
            ('service_type',
            'service_status'),
            ('dear',
            'mail_title'),
            'banns_date',
            ('bible','reader'),
            ('other',
            'other_reader'),
            ('by_license',
            'organ',
            'choir',
            'bells',
            'flowers',
            'video',
            'cd',
            'winter_heating',
            'verger',
            'car_park_attendant'),
            ('marches',
            'singing'),
            ('organist',
            'flowers_details'),
            'flowers_contact',
            ('no_of_guests',
            'wheelchair_access'),
            ('rehearsal_date',
            'rehearsal_time'),
            'total_paid',
            'date_amount_paid',
            'notes',
            ('first_visit',
            'second_visit'),
            'third_visit',
            ('evidence_filed',
            'decree_abs_seen'),
            'church_price',			
            'by_license_price',			
            'bells_price',			
            'cd_price',			
            'choir_price',			
            'car_park_attendant_price',			
            'flowers_price',			
            'organ_price',			
            'verger_price',			
            'video_price',			
            'winter_heating_price',			
            'banns_no',				
        ]		
	
admin.site.register(Wedding,Weedingsform)
admin.site.register(ServiceType)
admin.site.register(ServiceStatus)
#admin.site.register(additionalServices, WeedingaddtionalList)

