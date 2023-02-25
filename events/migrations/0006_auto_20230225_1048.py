# Generated by Django 3.2.6 on 2023-02-25 15:48

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0005_auto_20230225_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='interested',
            field=models.ManyToManyField(related_name='interested', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 26, 15, 48, 16, 367530, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2023, 2, 26, 15, 48, 16, 367547, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 25, 15, 48, 16, 367490, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2023, 2, 25, 15, 48, 16, 367517, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prize',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 26, 15, 48, 16, 369148, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prize',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2023, 2, 26, 15, 48, 16, 369161, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prize',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 25, 15, 48, 16, 369113, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prize',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2023, 2, 25, 15, 48, 16, 369131, tzinfo=utc)),
        ),
    ]
