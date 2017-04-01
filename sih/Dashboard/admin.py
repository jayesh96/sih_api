from django.contrib import admin

# Register your models here.

from .models import (
	PlaceLocation,
	GeographicalLocation
	)


admin.site.register(PlaceLocation)
admin.site.register(GeographicalLocation)