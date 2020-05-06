from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='event-home'),
    path('about/', views.about, name='event-about'),
    path('event_list/', views.event_list, name='event-event_list'),
    path('event/<int:id>/', views.view_event, name='event-view'),
    path('myevents/', views.my_events, name='event-my_events'),
    path('myevents/past', views.my_events_past, name='event-my_events_past'),
    path('myevents/<int:id>/delete', views.remove_my_event,
         name='event-remove_my_event'),

]
