from .models import DynamicPricing

def get_dynamic_price(bike_type, time_of_day, day_of_week, weather_condition=None):
    """
    Fetch dynamic pricing based on bike type, time, day, and weather.
    If weather is not provided, match only on other fields.
    """
    filters = {
        'bike_type': bike_type,
        'time_of_day': time_of_day,
        'day_of_week': day_of_week,
    }
    if weather_condition:
        filters['weather_condition'] = weather_condition

    return DynamicPricing.objects.filter(**filters).first()
