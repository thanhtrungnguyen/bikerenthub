from django.urls import path
from .apis import DynamicPricingDetailApi, DynamicPricingUpdateApi

urlpatterns = [
    path('dynamic-pricing/', DynamicPricingDetailApi.as_view(), name='dynamic-pricing-detail'),
    path('dynamic-pricing/update/', DynamicPricingUpdateApi.as_view(), name='dynamic-pricing-update'),
]
