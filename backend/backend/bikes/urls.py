from django.urls import path
from .apis import BikeListApi, BikeDetailApi, BikeUpdateStatusApi

urlpatterns = [
    path('', BikeListApi.as_view(), name='bike-list'),
    path('<uuid:bike_id>/', BikeDetailApi.as_view(), name='bike-detail'),
    path('<uuid:bike_id>/update-status/', BikeUpdateStatusApi.as_view(), name='bike-update-status'),
]
