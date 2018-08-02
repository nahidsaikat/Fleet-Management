from django.contrib import admin

from .fleet.models import Fleet
from .vehicle.models import Vehicle
from .vehicle.vehicle_log.models import VehicleLog
from .requisition.models import Requisition
from .requisition.requisition_log.models import RequisitionLog
from .comment.models import Comment
from .notification.models import Notification


admin.site.register(Fleet)
admin.site.register(Vehicle)
admin.site.register(VehicleLog)
admin.site.register(Requisition)
admin.site.register(RequisitionLog)
admin.site.register(Comment)
admin.site.register(Notification)
