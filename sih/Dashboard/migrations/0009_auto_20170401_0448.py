# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0008_auto_20170401_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geographicallocation',
            name='type',
            field=models.CharField(choices=[('airport', 'airport'), ('amusement_park', 'amusement_park'), ('aquarium', 'aquarium'), ('atm', 'atm'), ('bus_station', 'Bus Station'), ('casino', 'casino'), ('fire_station', 'fire_station'), ('gas_station', 'gas_station'), ('hindu_temple', 'hindu_temple'), ('library', 'library'), ('mosque', 'mosque'), ('movie_theater', 'movie_theater'), ('museum', 'museum'), ('night_club', 'night_club'), ('park', 'park'), ('police', 'police'), ('restaurant', 'restaurant'), ('shopping_mall', 'shopping_mall'), ('spa', 'spa'), ('stadium', 'stadium'), ('taxi_stand', 'taxi_stand'), ('train_station', 'train_station'), ('travel_agency', 'travel_agency'), ('zoo', 'zoo')], max_length=20),
        ),
    ]