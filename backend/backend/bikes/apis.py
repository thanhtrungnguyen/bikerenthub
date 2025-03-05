from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from django.http import Http404

from .models import BikeStatus
from .selectors import bike_get, bike_list
from .services import bike_update_status
from .serializers import BikeSerializer

class BikeListApi(APIView):
    def get(self, request):
        filters = request.query_params.dict()
        bikes = bike_list(filters=filters)
        data = BikeSerializer(bikes, many=True).data
        return Response(data)

class BikeDetailApi(APIView):
    def get_object(self, bike_id):
        bike = bike_get(bike_id)
        if bike is None:
            raise Http404
        return bike

    def get(self, request, bike_id):
        bike = self.get_object(bike_id)
        data = BikeSerializer(bike).data
        return Response(data)

class BikeUpdateStatusApi(APIView):
    class InputSerializer(serializers.Serializer):
        status = serializers.ChoiceField(choices=BikeStatus.choices)

    def post(self, request, bike_id):
        bike = bike_get(bike_id)
        if bike is None:
            raise Http404

        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        updated_bike = bike_update_status(bike=bike, status=serializer.validated_data['status'])
        return Response(BikeSerializer(updated_bike).data)
