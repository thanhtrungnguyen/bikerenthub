import django_filters
from .models import Bike

class BikeFilter(django_filters.FilterSet):
    class Meta:
        model = Bike
        fields = ('station', 'status', 'bike_type')
