from django.urls import path
from .apis import StationListApi, StationDetailApi, StationUpdateBikeCountApi

urlpatterns = [
    path('', StationListApi.as_view(), name='station-list'),
    path('<uuid:station_id>/', StationDetailApi.as_view(), name='station-detail'),
    path('<uuid:station_id>/update-bike-count/', StationUpdateBikeCountApi.as_view(), name='station-update-bike-count'),
]
