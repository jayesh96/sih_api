from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField,HyperlinkedRelatedField,SerializerMethodField
from Dashboard.models import PlaceLocation,GeographicalLocation


class PlaceLocationListSerializer(ModelSerializer):
	class Meta:
		model = PlaceLocation
		fields = ("id","longitude","latitude","name")


class PlaceLocationCreateSerializer(ModelSerializer):
	class Meta:
		model = PlaceLocation
		fields = ("id","longitude","latitude","name")
		

class PlaceLocationUpdateSerializer(ModelSerializer):
	class Meta:
		model = PlaceLocation
		fields = ("id","longitude","latitude","name")
		

class PlaceLocationRetrieveSerializer(ModelSerializer):
	class Meta:
		model = PlaceLocation
		fields = ("id","longitude","latitude","name")




class GeographicalLocationListSerializer(ModelSerializer):
	city = HyperlinkedRelatedField(read_only=True, view_name='location-retrieve')
	class Meta:
		model = GeographicalLocation
		fields = ("id","city","name","type","longitude","latitude","description","history")


class GeographicalLocationCreateSerializer(ModelSerializer):
	class Meta:
		model = GeographicalLocation
		fields = ("id","city","name","type","longitude","latitude","description","history")

class GeographicalLocationUpdateSerializer(ModelSerializer):
	class Meta:
		model = GeographicalLocation
		fields = ("id","city","name","type","longitude","latitude","description","history")
		

class GeographicalLocationRetrieveSerializer(ModelSerializer):
	class Meta:
		model = GeographicalLocation
		fields = ("id","city","name","type","longitude","latitude","description","history")