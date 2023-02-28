from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

class Prize(models.Model):
    prize_name = models.CharField(max_length=100)
    coins_required = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    # date_received = models.DateField(default=timezone.now())
    image = models.ImageField(upload_to='static/img/prize_images/', null=True, blank=True)
    can_be_redeemed = models.BooleanField(default=False)
    visibility = models.BooleanField(default=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    # pub_date = models.DateTimeField('date added')
    # start_date = models.DateField(default=timezone.now())
    # start_time = models.TimeField(default=timezone.now())
    # end_date = models.DateField(default=(timezone.now() + timezone.timedelta(1)))
    # end_time = models.TimeField(default=(timezone.now() + timezone.timedelta(1)))
    def __str__(self):
        return self.prize_name
    #def was_published_recently(self):
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

