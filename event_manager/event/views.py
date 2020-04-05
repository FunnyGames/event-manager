from django.shortcuts import render
from .models import Event

# Create your views here.


def home(request):
    context = {
        'events': Event.objects.all()
    }
    return render(request, 'event/home.html', context)


def about(request):
    return render(request, 'event/about.html', {'title': 'About'})


def event_list(request):
    return render(request, 'event/event_list.html', {'title': 'Event_List'})
