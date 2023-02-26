# Generated by Django 3.2.6 on 2023-02-26 17:15

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_auto_20230225_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 26, 17, 15, 35, 514387, tzinfo=utc), verbose_name='date added'),
        ),
        migrations.AlterField(
            model_name='prize',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 27, 17, 15, 35, 516425, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prize',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2023, 2, 27, 17, 15, 35, 516444, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prize',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 26, 17, 15, 35, 516394, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prize',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2023, 2, 26, 17, 15, 35, 516411, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_text', models.CharField(max_length=100)),
                ('colour', models.CharField(max_length=100)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
    ]
