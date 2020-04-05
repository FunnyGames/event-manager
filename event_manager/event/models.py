from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username
