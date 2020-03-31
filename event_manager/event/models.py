from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
