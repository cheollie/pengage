# Generated by Django 3.2.6 on 2023-02-25 22:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_auto_20230225_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 25, 22, 42, 41, 11454, tzinfo=utc), verbose_name='date added'),
        ),
        migrations.AlterField(
            model_name='prize',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 26, 22, 42, 41, 13138, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prize',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2023, 2, 26, 22, 42, 41, 13154, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prize',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 25, 22, 42, 41, 13109, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prize',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2023, 2, 25, 22, 42, 41, 13124, tzinfo=utc)),
        ),
    ]
