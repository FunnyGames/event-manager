from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='event-home'),
    path('about/', views.about, name='event-about'),
    path('event_list/', views.event_list, name='event-event_list'),
    path('event/<int:id>/', views.view_event, name='event-view'),
    path('event/delete-comment/<int:id>/',
         views.delete_comment, name='delete_comment'),
    path('event/report-comment/<int:id>/',
         views.report_comment, name='report_comment'),
    path('myevents/', views.my_events, name='event-my_events'),
    path('myevents/past', views.my_events_past, name='event-my_events_past'),
    path('myevents/<int:id>/delete', views.remove_my_event,
         name='event-remove_my_event'),

]
