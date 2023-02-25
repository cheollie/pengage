# Generated by Django 3.2.6 on 2023-02-25 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20230225_1404'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='events_interested',
            field=models.ManyToManyField(blank=True, to='events.Event'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='grade',
            field=models.IntegerField(choices=[(9, 9), (10, 10), (11, 11), (12, 12)]),
        ),
    ]
