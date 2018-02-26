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
	
	
admin.site.register(Wedding,Weedingsform)
admin.site.register(ServiceType)
admin.site.register(ServiceStatus)
#admin.site.register(additionalServices, WeedingaddtionalList)

