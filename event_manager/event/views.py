from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from .models import Event
from .models import CancelledEvent
from .models import EventUpdates

# Create your views here.

Event = Event.objects.all()
CancelledEvent = CancelledEvent.objects.all()
UpdatesEvent = EventUpdates.objects.all()


def home(request):
    return render(request, 'event/home.html')


def about(request):
    return render(request, 'event/about.html', {'title': 'About'})


def event_list(request):
    context = {
        'events': Event,
        'announcements': UpdatesEvent,
        'cancelled_events': CancelledEvent
    }
    return render(request, 'event/event_list.html', context)
