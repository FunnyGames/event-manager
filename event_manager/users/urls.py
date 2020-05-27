from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('users/', views.users, name='users-list'),
    path('reset/', views.resetPassword, name='users-reset'),
]
