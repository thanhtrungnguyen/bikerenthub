import django_filters
from .models import Station

class StationFilter(django_filters.FilterSet):
    class Meta:
        model = Station
        fields = ['name']
