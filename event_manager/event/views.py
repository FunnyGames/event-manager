from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from .models import Event
from .models import CancelledEvent
from .models import EventUpdates

# Create your views here.

def home(request):
    return render(request, 'event/home.html')


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'event/about.html', context)


def event_list(request):
    context = {
        'events': Event.objects.all(),
        'announcements': EventUpdates.objects.all(),
        'cancelled_events': CancelledEvent.objects.all()
    }
    return render(request, 'event/event_list.html', context)


def view_event(request, id):
    context = {
        'event': Event.objects.get(id=id),
        'announcements': EventUpdates.objects.filter(EventId=id),
        'cancelled_event': CancelledEvent.objects.filter(EventId=id)
    }
    return render(request, 'event/event.html', context)
