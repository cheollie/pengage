import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
from django import forms
import uuid

class Tag(models.Model):
    tag = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    def __str__(self):
        return self.tag

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
    location = models.CharField(max_length=200, default="School")
    image = models.ImageField(upload_to='static/img/event_images/', null=True, blank=True)
    interested = models.ManyToManyField(User, blank=True, related_name='interested')
    participants = models.ManyToManyField(User, blank=True, related_name='participants')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    tags = models.ManyToManyField(Tag, blank=True)
    visibility = models.BooleanField(default=False)
    points_propagated = models.BooleanField(default=False)
    
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
