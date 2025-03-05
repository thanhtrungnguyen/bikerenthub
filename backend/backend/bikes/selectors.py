from .models import Bike
from .filters import BikeFilter

def bike_list(*, filters=None):
    filters = filters or {}
    qs = Bike.objects.all()
    return BikeFilter(filters, qs).qs

def bike_get(bike_id):
    return Bike.objects.filter(id=bike_id).first()

def get_bikes_by_station(station_id):
    return Bike.objects.filter(station_id=station_id)

def get_bikes_with_station():
    return Bike.objects.select_related("station").all()
