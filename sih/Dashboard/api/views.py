from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView,RetrieveUpdateDestroyAPIView

from Dashboard.api.serializers import (
    # products serializer
    PlaceLocationListSerializer,
PlaceLocationCreateSerializer,
PlaceLocationUpdateSerializer,
PlaceLocationRetrieveSerializer,
GeographicalLocationListSerializer,
GeographicalLocationCreateSerializer,
GeographicalLocationUpdateSerializer,
GeographicalLocationRetrieveSerializer,
)

from Dashboard.models import PlaceLocation,GeographicalLocation


class PlaceLocationList(ListAPIView):
	queryset = PlaceLocation.objects.all()
	serializer_class = PlaceLocationListSerializer	


class PlaceLocationCreate(CreateAPIView):
	queryset = PlaceLocation.objects.all()
	serializer_class = PlaceLocationCreateSerializer	


class PlaceLocationRetrive(RetrieveAPIView):
	queryset = PlaceLocation.objects.all()
	serializer_class = PlaceLocationRetrieveSerializer
	


class PlaceLocationUpdate(RetrieveUpdateDestroyAPIView):
	queryset = PlaceLocation.objects.all()
	serializer_class = PlaceLocationUpdateSerializer
	


class GeographicalLocationList(ListAPIView):
	queryset = GeographicalLocation.objects.all()
	serializer_class = GeographicalLocationListSerializer


class GeographicalLocationCreate(CreateAPIView):
	queryset = GeographicalLocation.objects.all()
	serializer_class = GeographicalLocationCreateSerializer

	

class GeographicalLocationRetrieve(RetrieveAPIView):
	queryset = GeographicalLocation.objects.all()
	serializer_class = GeographicalLocationRetrieveSerializer
	

class GeographicalLocationUpdate(RetrieveUpdateDestroyAPIView):
	queryset = GeographicalLocation.objects.all()
	serializer_class = GeographicalLocationUpdateSerializer
	