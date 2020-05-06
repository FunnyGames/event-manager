from django.contrib import admin
from .models import Event
from .models import CancelledEvent
from .models import EventUpdates
from .models import RateEvent
from .models import MyEvent

# Register your models here.
admin.site.register(Event)
admin.site.register(CancelledEvent)
admin.site.register(EventUpdates)
admin.site.register(RateEvent)
admin.site.register(MyEvent)
