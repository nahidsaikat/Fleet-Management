from django.contrib import admin

from .fleet.models import Fleet
from .vehicle.models import Vehicle
from .requisition.models import Requisition


admin.site.register(Fleet)
admin.site.register(Vehicle)
admin.site.register(Requisition)
