from django.contrib import admin
from .models import Wedding, ServiceStatus, ServiceType,additionalServices

# Register your models here.


class WeedingaddtionalList(admin.ModelAdmin):
	list_display = ["name","current_price","upcoming_price","upcoming_date"]



admin.site.register(Wedding)
admin.site.register(ServiceType)
admin.site.register(ServiceStatus)
admin.site.register(additionalServices, WeedingaddtionalList)

