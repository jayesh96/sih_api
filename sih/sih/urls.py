"""sih URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns


from Dashboard.api.views import (
	PlaceLocationList,
	PlaceLocationCreate,
	PlaceLocationRetrive,
	PlaceLocationUpdate,
	GeographicalLocationList,
	GeographicalLocationCreate,
	GeographicalLocationRetrieve,
	GeographicalLocationUpdate,
	)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/location/list/$', PlaceLocationList.as_view(), name='location-list'), 
    url(r'^api/location/create/$', PlaceLocationCreate.as_view(), name='location-create'), 
    url(r'^api/location/retrieve/(?P<pk>[\d]+)/$', PlaceLocationRetrive.as_view(), name='location-retrieve'), 
    url(r'^api/location/update/(?P<pk>[\d]+)/$', PlaceLocationUpdate.as_view(), name='location-update'), 
    url(r'^api/geolocation/list/$', GeographicalLocationList.as_view(), name='geolocation-list'), 
    url(r'^api/geolocation/create/$', GeographicalLocationCreate.as_view(), name='geolocation-create'), 
    url(r'^api/geolocation/retrieve/(?P<pk>[\d]+)/$', GeographicalLocationRetrieve.as_view(), name='geolocation-retrieve'), 
    url(r'^api/geolocation/update/(?P<pk>[\d]+)/$', GeographicalLocationUpdate.as_view(), name='geolocation-update	'), 
    
]

urlpatterns = format_suffix_patterns(urlpatterns)

