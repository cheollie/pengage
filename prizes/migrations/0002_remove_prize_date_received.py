# Generated by Django 3.2.6 on 2023-02-27 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prizes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prize',
            name='date_received',
        ),
    ]