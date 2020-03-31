from django.shortcuts import render
from .models import Event

# Create your views here.
events = [
    {
        'title': 'Purim',
        'date': '10/03/20',
        'description': 'Purim party'
    },
    {
        'title': 'Coldplay',
        'date': '22/03/20',
        'description': 'Concert of Coldplay'
    }
]


def home(request):
    context = {
        'events': Event.objects.all()
    }
    return render(request, 'event/home.html', context)


def about(request):
    return render(request, 'event/about.html', {'title': 'About'})
