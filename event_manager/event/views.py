from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import connection
from .models import Event
from .models import CancelledEvent
from .models import EventUpdates
from .models import RateEvent
from .models import MyEvent
from .models import EventComment
from django.db.models import Avg
from .forms import RateEventForm, eventCommentForm
from datetime import date

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

    ratingForm = None
    commentForm = eventCommentForm()
    my_rating = None
    my_event = []



    if request.user.id:
        my_event = MyEvent.objects.filter(EventId=id, user=request.user)
        my_rating = (RateEvent.objects.filter(
            user=request.user).filter(EventId=id).first())
        if my_rating == None:
            if request.method == 'POST' and 'rating_post' in request.POST:
                ratingForm = RateEventForm(request.POST)

                if ratingForm.is_valid():
                    rating = ratingForm.save(commit=False)
                    if rating.user_id is None:
                        rating.user_id = request.user.id
                        rating.EventId = id
                    rating.save()
                    my_rating = (RateEvent.objects.filter(
                        user=request.user).filter(EventId=id).first())
            else:
                ratingForm = RateEventForm()


    context = {
        'event': get_object_or_404(Event, id=id),
        'announcements': EventUpdates.objects.filter(EventId=id),
        'cancelled_event': CancelledEvent.objects.filter(EventId=id),
        'registered_users': MyEvent.objects.filter(EventId=id).count(),
        'ratings_counts': RateEvent.objects.filter(EventId=id).count(),
        'ratings_avg': RateEvent.objects.filter(EventId=id).aggregate(Avg('rate')),
        'my_rating': my_rating,
        'comments': EventComment.objects.all().filter(EventId=id),
        'my_event': my_event,
        'ratingForm': ratingForm, 
        'commentForm': commentForm
    }

    return render(request, 'event/event.html', context)


@login_required
def my_events(request):
    if request.method == 'POST':
        eventId = request.POST.get('EventId', None)
        if (eventId != None):
            MyEvent.objects.create(EventId=eventId, user=request.user)
            messages.success(
                request, f'Event was added to your events successfully')

    context = {
        'events': Event.objects.filter(create_date__gte=date.today()),
        'announcements': EventUpdates.objects.all(),
        'cancelled_events': CancelledEvent.objects.all(),
        'my_events': MyEvent.objects.filter(user_id=request.user.id)
    }
    return render(request, 'event/my_events.html', context)


@login_required
def my_events_past(request):
    context = {
        'events': Event.objects.filter(create_date__lte=date.today()),
        'announcements': EventUpdates.objects.all(),
        'cancelled_events': CancelledEvent.objects.all(),
        'my_events': MyEvent.objects.filter(user_id=request.user.id)
    }
    return render(request, 'event/my_events.html', context)


@login_required
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
