from django import forms
from .models import CancelledEvent, EventUpdates, RateEvent, EventComment
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

class eventCommentForm(forms.ModelForm):
    text = forms.CharField(
        max_length=200,
        label="Write Comment:",
        widget=forms.Textarea(attrs={'style':'max-width: 25em'}))

    class Meta:
        model = EventComment
        fields = ['text']

