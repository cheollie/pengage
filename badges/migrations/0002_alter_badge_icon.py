# Generated by Django 3.2.6 on 2023-02-28 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='icon',
            field=models.ImageField(upload_to='static/img/badge_images/'),
        ),
    ]
