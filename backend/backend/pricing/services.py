from .models import DynamicPricing
from .selectors import get_dynamic_price


def calculate_price(bike_type, time_of_day, day_of_week, base_price, weather_condition=None):
    """
    Fetch dynamic price adjustment and calculate the final price per minute.
    """
    pricing = get_dynamic_price(bike_type, time_of_day, day_of_week, weather_condition)

    if pricing and pricing.ai_adjusted_price:
        return pricing.ai_adjusted_price

    # Fallback if no dynamic pricing found
    return base_price

def update_dynamic_pricing(*, bike_type, time_of_day, day_of_week, weather_condition, base_price, ai_adjusted_price=None):
    """
    Upsert dynamic pricing entry.
    """
    pricing, _ = DynamicPricing.objects.update_or_create(
        bike_type=bike_type,
        time_of_day=time_of_day,
        day_of_week=day_of_week,
        weather_condition=weather_condition,
        defaults={'base_price': base_price, 'ai_adjusted_price': ai_adjusted_price}
    )
    return pricing
