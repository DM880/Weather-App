# Generated by Django 3.2 on 2021-10-03 14:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('city_weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='searche',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
