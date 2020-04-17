from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now=False, null=True)
    end_date = models.DateTimeField(auto_now=False, null=True)
    capacity = models.IntegerField(default=0)
    place = models.CharField(max_length=120, default="-")
    cancelled = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CancelledEvent(models.Model):
    EventId = models.IntegerField(default=0)

    def __str__(self):
        return str(self.EventId)


class EventUpdates(models.Model):
    EventId = models.IntegerField(default=0)
    announcement = models.TextField()
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.EventId)
