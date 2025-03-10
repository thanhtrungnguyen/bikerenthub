from django.urls import path
from .apis import BikeListApi, BikeDetailApi, BikeUpdateStatusApi

app_name = 'bikes'

urlpatterns = [
    path('', BikeListApi.as_view(), name='bike-list'),
    path('<int:bike_id>/', BikeDetailApi.as_view(), name='bike-detail'),
    path('<int:bike_id>/update-status/', BikeUpdateStatusApi.as_view(), name='bike-update-status'),
]
