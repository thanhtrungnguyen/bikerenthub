from django.urls import path
from .apis import StationListApi,StationCreateApi,StationGetByIdApi, StationDetailApi, StationRetrieveUpdateApi

app_name = 'stations'

urlpatterns = [
    path('', StationListApi.as_view(), name='station-list'),
    # path('', StationGetByIdApi.as_view(), name='station-list'),
    path('<int:station_id>/', StationDetailApi.as_view(), name='station-detail'),
    path('<int:station_id>/update/', StationRetrieveUpdateApi.as_view(), name='station-update'),
    path('create', StationCreateApi.as_view(), name='station-create'),
]
