from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='event-home'),
    path('about/', views.about, name='event-about'),
    path('event_list/', views.event_list, name='event-event_list'),
    path('event/<int:id>/', views.view_event, name='event-view'),

]
