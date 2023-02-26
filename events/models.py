import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
from django import forms
import uuid

class Event(models.Model):
    event_title = models.CharField(max_length=200)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True}, related_name='organizer')
    pub_date = models.DateTimeField('date added', default=timezone.now())
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    points = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    interested = models.ManyToManyField(User, blank=True, related_name='interested')
    participants = models.ManyToManyField(User, blank=True, related_name='participants')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    visibility = models.BooleanField(default=False)
    
    def __str__(self):
        return self.event_title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    #def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if end_date < start_date:
            raise forms.ValidationError("End date should be greater than start date.")
        if start_date == end_date:
            start_time = cleaned_data.get("start_time")
            end_time = cleaned_data.get("end_time")
            if end_time < start_time:
                raise forms.ValidationError("End time should be greater than start time.")
        return {'start_date': start_date, 'end_date': end_date, 'start_time': start_time, 'end_time': end_time}

class Tag(models.Model):
    tag = models.CharField(max_length=100)
    # colour = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    def __str__(self):
        return self.tag

"""
# not checked / temp rn
class Participation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participation_date = models.DateField(auto_now_add=True)
    
# not checked temp rn
class Point(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    points = models.IntegerField()
    point_date = models.DateField(auto_now_add=True)
"""

class Prize(models.Model):
    prizes_text = models.CharField(max_length=100)
    points_required = models.IntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='prize_images/', null=True) 
    pub_date = models.DateTimeField('date added')
    start_date = models.DateField(default=timezone.now())
    start_time = models.TimeField(default=timezone.now())
    end_date = models.DateField(default=(timezone.now() + timezone.timedelta(1)))
    end_time = models.TimeField(default=(timezone.now() + timezone.timedelta(1)))
    visibility = models.BooleanField(default=False)
    def __str__(self):
        return self.prizes_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    #def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if end_date < start_date:
            raise forms.ValidationError("End date should be greater than start date.")
        if start_date == end_date:
            start_time = cleaned_data.get("start_time")
            end_time = cleaned_data.get("end_time")
            if end_time < start_time:
                raise forms.ValidationError("End time should be greater than start time.")
        return {'start_date': start_date, 'end_date': end_date, 'start_time': start_time, 'end_time': end_time}
    #have a function where owner on demand can pick winner(s) from one of the presets
    #   - on random draw
    #   - on most points (in range of dates) / top (x) etc
    #give prize to user (set winner[s])
