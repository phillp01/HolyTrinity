from django.contrib import admin
from .models import Wedding, ServiceStatus, ServiceType

# Register your models here.

admin.site.register(Wedding)
admin.site.register(ServiceType)
admin.site.register(ServiceStatus)

