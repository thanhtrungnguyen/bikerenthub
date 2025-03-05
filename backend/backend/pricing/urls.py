from django.urls import path
from .apis import DynamicPricingDetailApi, DynamicPricingUpdateApi

app_name = 'pricing'

urlpatterns = [
    path('dynamic-pricing/', DynamicPricingDetailApi.as_view(), name='dynamic-pricing-detail'),
    path('dynamic-pricing/update/', DynamicPricingUpdateApi.as_view(), name='dynamic-pricing-update'),
]
