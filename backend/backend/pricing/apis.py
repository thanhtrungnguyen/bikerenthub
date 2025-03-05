from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .selectors import get_dynamic_price
from .services import update_dynamic_pricing
from .serializers import DynamicPricingSerializer

from .models import DynamicPricing

class DynamicPricingDetailApi(APIView):
    """
    Get a dynamic pricing rule based on criteria.
    """

    class InputSerializer(serializers.Serializer):
        bike_type = serializers.CharField(max_length=50)
        time_of_day = serializers.CharField(max_length=10)
        day_of_week = serializers.IntegerField(min_value=0, max_value=6)
        weather_condition = serializers.CharField(max_length=50, required=False)

    def get(self, request):
        serializer = self.InputSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        price_rule = get_dynamic_price(
            bike_type=serializer.validated_data['bike_type'],
            time_of_day=serializer.validated_data['time_of_day'],
            day_of_week=serializer.validated_data['day_of_week'],
            weather_condition=serializer.validated_data.get('weather_condition')
        )

        if not price_rule:
            return Response({'detail': 'No pricing rule found'}, status=status.HTTP_404_NOT_FOUND)

        return Response(DynamicPricingSerializer(price_rule).data)


class DynamicPricingUpdateApi(APIView):
    """
    Create or update a dynamic pricing rule.
    """

    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            model = DynamicPricing
            fields = [
                'bike_type', 'time_of_day', 'day_of_week', 'weather_condition',
                'base_price', 'ai_adjusted_price'
            ]

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        updated_rule = update_dynamic_pricing(
            **serializer.validated_data
        )

        return Response(DynamicPricingSerializer(updated_rule).data, status=status.HTTP_200_OK)
