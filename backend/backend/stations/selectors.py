from .models import Station
from .filters import StationFilter

def station_list(*, filters=None):
    filters = filters or {}
    qs = Station.objects.all()
    return StationFilter(filters, qs).qs

def station_get(*, station_id):
    return Station.objects.filter(id=station_id).first()
