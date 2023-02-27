from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    grade = models.IntegerField(choices=[(i, i) for i in range(9, 13)], default=11)
    points_alltime = models.IntegerField(default=0)
    points_quarterly = models.IntegerField(default=0)
    coins = models.IntegerField(default=0)
    events_interested = models.ManyToManyField('events.Event', related_name='interested+', blank=True)
    events_participated = models.ManyToManyField('events.Event', related_name='participated+', blank=True)
    tags_interested = models.ManyToManyField('events.Tag', blank=True)
    prizes_redeemed = models.ManyToManyField('prizes.Prize', blank=True)
    badges_earned = models.ManyToManyField('badges.Badge', blank=True)
    is_private = models.BooleanField(default=False)

