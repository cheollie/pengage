from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    grade = models.IntegerField(choices=[(i, i) for i in range(9, 13)], default=9)
    points = models.IntegerField(default=0)
    events_interested = models.ManyToManyField('events.Event', blank=True)
