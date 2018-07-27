from django.contrib import admin

from .fleet.models import Fleet
from .vehicle.models import Vehicle
from .requisition.models import Requisition
from .comment.models import Comment
from .notification.models import Notification


admin.site.register(Fleet)
admin.site.register(Vehicle)
admin.site.register(Requisition)
admin.site.register(Comment)
admin.site.register(Notification)
