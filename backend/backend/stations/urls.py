from django.urls import path
from .apis import StationListCreateApi, StationDetailApi, StationRetrieveUpdateApi

app_name = 'stations'

urlpatterns = [
    path('', StationListCreateApi.as_view(), name='station-list'),
    path('<int:station_id>/', StationDetailApi.as_view(), name='station-detail'),
    path('<int:station_id>/update/', StationRetrieveUpdateApi.as_view(), name='station-update'),
    # path('')
]
