from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import connection
from .models import Event
from .models import CancelledEvent
from .models import EventUpdates
from .models import RateEvent
from .models import MyEvent
from django.db.models import Avg
from .forms import RateEventForm

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

    form = None
    my_rating = None

    if request.user.id:
        my_rating = (RateEvent.objects.filter(
            user=request.user).filter(EventId=id).first())
        if my_rating == None:
            if request.method == 'POST':
                form = RateEventForm(request.POST)

                if form.is_valid():
                    rating = form.save(commit=False)
                    if rating.user_id is None:
                        rating.user_id = request.user.id
                        rating.EventId = id
                    rating.save()
                    my_rating = (RateEvent.objects.filter(
                        user=request.user).filter(EventId=id).first())
            else:
                form = RateEventForm()

    context = {
        'event': get_object_or_404(Event, id=id),
        'announcements': EventUpdates.objects.filter(EventId=id),
        'cancelled_event': CancelledEvent.objects.filter(EventId=id),
        'registered_users': 1,  # placeholder for future use
        'ratings_counts': RateEvent.objects.filter(EventId=id).count(),
        'ratings_avg': RateEvent.objects.filter(EventId=id).aggregate(Avg('rate')),
        'my_rating': my_rating,
        'my_event': MyEvent.objects.filter(EventId=id),
        'form': form
    }

    return render(request, 'event/event.html', context)


def my_events(request):
    if request.method == 'POST':
        eventId = request.POST.get('EventId', None)
        if (eventId != None):
            x = MyEvent.objects.create(EventId=eventId, user=request.user)
            messages.success(
                request, f'Event was added to your events successfully')

    context = {
        'events': Event.objects.all(),
        'announcements': EventUpdates.objects.all(),
        'cancelled_events': CancelledEvent.objects.all(),
        'my_events': MyEvent.objects.filter(user_id=request.user.id)
    }
    return render(request, 'event/my_events.html', context)


def remove_my_event(request, id):
    if request.method == 'POST':
        myId = request.POST.get('id', None)
        if (myId != None):
            MyEvent.objects.filter(
                id=myId, user_id=request.user.id, EventId=id).delete()

            messages.success(
                request, f'Event was removed from your events successfully')
            return redirect('event-my_events')
    context = {
        'event': get_object_or_404(Event, id=id),
        'my_events': MyEvent.objects.filter(user_id=request.user.id, EventId=id)
    }
    return render(request, 'event/confirm_remove_my_event.html', context)
