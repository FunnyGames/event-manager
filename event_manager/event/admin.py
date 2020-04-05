from django.contrib import admin
from .models import Event
from .models import UserProfileInfo
# Register your models here.
admin.site.register(Event)
admin.site.register(UserProfileInfo)
