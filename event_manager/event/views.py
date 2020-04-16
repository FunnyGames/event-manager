from django.shortcuts import render
from .models import Event
from .models import CancelledEvent

# Create your views here.

Event = Event.objects.all()
CancelledEvent = CancelledEvent.objects.all()

def home(request):
    context = {
        'events': Event.exclude(id__in=CancelledEvent)
    }
    return render(request, 'event/home.html', context)


def about(request):
    return render(request, 'event/about.html', {'title': 'About'})


def event_list(request):
    return render(request, 'event/event_list.html', {'title': 'Event_List'})
