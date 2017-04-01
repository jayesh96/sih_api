from __future__ import unicode_literals

from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ("airport", "airport"),
    ("amusement_park", "amusement_park"),
    ("aquarium", "aquarium"),
    ("atm","atm"),
    ("bus_station","Bus Station"),
    ("casino","casino"),
    ("fire_station","fire_station"),
    ("gas_station","gas_station"),
    ("hindu_temple","hindu_temple"),
    ("library","library"),
    ("mosque","mosque"),
    ("movie_theater","movie_theater"),
    ("museum","museum"),
    ("night_club","night_club"),
    ("park","park"),
    ("police","police"),
    ("restaurant","restaurant"),
    ("shopping_mall","shopping_mall"),
    ("spa","spa"),
    ("stadium","stadium"),
    ("taxi_stand","taxi_stand"),
    ("train_station","train_station"),
    ("travel_agency","travel_agency"),
    ("zoo","zoo"),

 
)


class PlaceLocation(models.Model):
    id = models.AutoField(primary_key=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    name = models.CharField(max_length=200, null=False, blank=False, default="")
    
    def __str__(self):
        return self.name

    def __unicode__(self):
        return str(self.name)

 
class GeographicalLocation(models.Model):
	id = models.AutoField(primary_key=True)
	city = models.ForeignKey(PlaceLocation,on_delete=models.CASCADE)
	name = models.CharField(max_length=120, null=False, blank=False, default="")
	type = models.CharField(max_length=20,choices=STATUS_CHOICES)
	longitude = models.DecimalField(max_digits=8, decimal_places=3)
	latitude = models.DecimalField(max_digits=8, decimal_places=3)
	description = models.TextField(null=True, blank=True)
	history = models.TextField(null=True, blank=True)


	def __str__(self):
		return str(self.name)

	def __unicode__(self):
		return str(self.name)

