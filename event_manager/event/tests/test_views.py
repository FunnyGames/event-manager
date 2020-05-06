from django.test import TestCase
from django.urls import reverse
from ..models import Event, CancelledEvent, EventUpdates,RateEvent,MyEvent
from django.contrib.auth.models import User

class ViewEventTest(TestCase):
    def setUp(self):
        test_event_1 = Event.objects.create(
            title='Event 1',
            description='Desc 1',
            start_date='2000-01-01 10:00',
            end_date='2000-01-01 12:00',
            capacity=100,
            place='tel-aviv'
        )
        test_event_1.save()

        test_event_2 = Event.objects.create(
            title='Event 2',
            description='Desc 2',
            start_date='2003-01-01 10:00',
            end_date='2003-01-01 12:00',
            capacity=200,
            place='tel-aviv'
        )
        test_event_2.save()

        test_cancelled_event = CancelledEvent.objects.create(EventId=1)
        test_cancelled_event.save()
        
        test_rate_event = RateEvent.objects.create(EventId=2,user=User.objects.create(
            username='test1', email='test@email.com', first_name='Big', last_name='Bob'),rate=5)
        test_rate_event.save()

        test_event_update = EventUpdates.objects.create(EventId=2, announcement='ann test')
        test_event_update.save()
        
        test_my_events = MyEvent.objects.create(EventId=2,user=User.objects.create(
            username='test2', email='test2@email.com', first_name='Big2', last_name='Bob2'))
        test_my_events.save()
        
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('event-view', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('event-view', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event/event.html')

    def test_view_not_found(self):
        response = self.client.get(reverse('event-view', args=[1000]))
        self.assertEqual(response.status_code, 404)



