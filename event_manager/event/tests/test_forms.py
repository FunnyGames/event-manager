from django.test import TestCase
from ..forms import RateEventForm

class RateEventFormTest(TestCase):

    def test_valid_data(self):
        data = {'rate': 4}
        form = RateEventForm(data)
        self.assertTrue(form.is_valid())

    
    def test_invalid_data(self):
        data = {'rate': 6}
        form = RateEventForm(data)
        self.assertFalse(form.is_valid())

    def test_required_missing(self):
        data = {}
        form = RateEventForm(data)
        self.assertFalse(form.is_valid())


 