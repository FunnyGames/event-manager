from django import forms
from .models import CancelledEvent, EventUpdates, RateEvent
from django.core.validators import MaxValueValidator, MinValueValidator

RATE_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]


class RateEventForm(forms.ModelForm):

    rate = forms.CharField(label='Rate Event:',
                           widget=forms.RadioSelect(choices=RATE_CHOICES))

    class Meta:
        model = RateEvent
        fields = ['rate']
