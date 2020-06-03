from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db import connection
from .models import Event
from .models import CancelledEvent
from .models import EventUpdates
from .models import RateEvent
from .models import MyEvent
from .models import EventComment
from .models import EventRecommend
from .models import ReportComment
from .models import ChooseComment
from django.db.models import Avg
from .forms import RateEventForm, eventCommentForm, eventRecommendForm
from datetime import date, timedelta

# Create your views here.


def home(request):
    return render(request, 'event/home.html')


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'event/about.html', context)


def event_list(request):
    page = request.GET.get('page')
    limit = request.GET.get('limit')
    if limit == None:
        limit = 5
    else:
        limit = int(limit)
        if limit < 1 or limit > 20:
            limit = 5

    p = Paginator(Event.objects.all(), limit)
    if page == None:
        page = 1
    else:
        page = int(page)
        if page < 1 or page > p.num_pages:
            page = 1
    context = {
        'page_obj': p.get_page(page),
        'announcements': EventUpdates.objects.all(),
        'cancelled_events': CancelledEvent.objects.all()
    }
    return render(request, 'event/event_list.html', context)


def recommended_event_list(request):
    context = {
        'events': Event.objects.filter(start_date__gte=date.today()),
        'announcements': EventUpdates.objects.all(),
        'cancelled_events': CancelledEvent.objects.all(),
        'recommended_events': EventRecommend.objects.all()
    }
    return render(request, 'event/recommended_event_list.html', context)


def view_event(request, id):

    ratingForm = None
    commentForm = eventCommentForm()
    recommendForm = eventRecommendForm()
    my_rating = None
    my_event = []

    if request.method == 'POST' and 'comment_post' in request.POST:
        commentForm = eventCommentForm(request.POST)
        if commentForm.is_valid():
            comment = commentForm.save(commit=False)
            comment.user_id = request.user.id
            comment.EventId = id
            comment.save()
            return redirect('event-view', id=id)

    if request.method == 'POST' and 'recommend_post' in request.POST:
        recommendForm = eventRecommendForm(request.POST)
        if recommendForm.is_valid():
            recommend = recommendForm.save(commit=False)
            recommend.user_id = request.user.id
            recommend.EventId = id
            recommend.save()
            return redirect('event-view', id=id)

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
        'recommends': EventRecommend.objects.all().filter(EventId=id),
        'my_event': my_event,
        'ratingForm': ratingForm,
        'commentForm': commentForm,
        'recommendForm': recommendForm,
        'reports': ReportComment.objects.filter(EventId=id),
        'chooseComment': ChooseComment.objects.filter(EventId=id)

    }

    return render(request, 'event/event.html', context)


def top_rated_list(request):

    events = Event.objects.all()
    rating = RateEvent.objects.values('EventId').annotate(
        aRate=Avg('rate')).order_by('-aRate')[:5]

    print(rating)
    context = {
        'events': Event.objects.all(),
        'announcements': EventUpdates.objects.all(),
        'cancelled_events': CancelledEvent.objects.all(),
        'events_avg_rating': rating
    }
    return render(request, 'event/top_rate_list.html', context)


@login_required
def choose_comment(request, id):
    try:
        comment = EventComment.objects.get(id=id)
        EventId = comment.EventId
        if (EventId != None):
            ChooseComment.objects.create(
                EventId=EventId, CommentId=comment, user=request.user)
            messages.success(
                request, f'LIKE Comment Successfull')
    except:
        messages.warning(
            request, f'ERROR - You are already liked this comment')

    return redirect('event-view', id=EventId)


@login_required
def my_events(request):
    if request.method == 'POST':
        eventId = request.POST.get('EventId', None)
        if (eventId != None):
            MyEvent.objects.create(EventId=eventId, user=request.user)
            messages.success(
                request, f'Event was added to your events successfully')

    context = {
        'events': Event.objects.filter(start_date__gte=date.today()),
        'announcements': EventUpdates.objects.all(),
        'cancelled_events': CancelledEvent.objects.all(),
        'my_events': MyEvent.objects.filter(user_id=request.user.id)
    }
    return render(request, 'event/my_events.html', context)


@login_required
def my_events_past(request):
    context = {
        'events': Event.objects.filter(start_date__lte=date.today()),
        'announcements': EventUpdates.objects.all(),
        'cancelled_events': CancelledEvent.objects.all(),
        'my_events': MyEvent.objects.filter(user_id=request.user.id)
    }
    return render(request, 'event/my_events.html', context)


@login_required
def my_events_all(request):
    context = {
        'events': Event.objects.all(),
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


@login_required
def delete_comment(request, id):
    comment = EventComment.objects.get(id=id)
    EventId = comment.EventId
    if (id != None):
        EventComment.objects.filter(
            id=id).delete()

    return redirect('event-view', id=EventId)


@login_required
def report_comment(request, id):
    try:
        comment = EventComment.objects.get(id=id)
        EventId = comment.EventId
        if (EventId != None):
            ReportComment.objects.create(
                EventId=EventId, CommentId=comment, user=request.user)
            messages.success(
                request, f'Comment Reported Successfully')
    except:
        messages.warning(
            request, f'ERROR - Already Reported?')

    return redirect('event-view', id=EventId)


@login_required
def calendar(request):
    events = Event.objects.filter(
        start_date__gte=date.today()).order_by('start_date')

    my_events = MyEvent.objects.filter(user_id=request.user.id)
    cancelled_events = CancelledEvent.objects.all()

    ev = []
    year_break = []
    month_break = []
    year = 0
    month = 0
    for e in events:
        for my in my_events:
            cancelled = False
            for can in cancelled_events:
                if e.id == can.EventId:
                    cancelled = True
                    break
            if cancelled:
                continue
            if e.id == my.EventId:
                ev.append(e)
                if year != e.start_date.year:
                    year = e.start_date.year
                    year_break.append(e.id)
                    month = 0
                if month != e.start_date.month:
                    breakm = month != 0
                    month = e.start_date.month
                    month_break.append({'id': e.id, 'break': breakm})

    context = {
        'events': ev,
        'year_break': year_break,
        'month_break': month_break
    }
    return render(request, 'event/calendar.html', context)


def users_attend(request, id):
    context = {
        'event': get_object_or_404(Event, id=id),
        'users': MyEvent.objects.filter(EventId=id)
    }
    return render(request, 'event/users_attend.html', context)
