from django.contrib import admin

from .fleet.models import Fleet
from .vehicle.models import Vehicle


admin.site.register(Fleet)
admin.site.register(Vehicle)
