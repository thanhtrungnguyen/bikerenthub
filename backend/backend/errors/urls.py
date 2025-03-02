from django.urls import path

from .apis import (
    TriggerErrorApi,
    TriggerUnhandledExceptionApi,
    TriggerValidateUniqueErrorApi,
)

app_name = "errors"

urlpatterns = [
    path("trigger/", TriggerErrorApi.as_view()),
    path("trigger/unique/", TriggerValidateUniqueErrorApi.as_view()),
    path("trigger/exception/", TriggerUnhandledExceptionApi.as_view()),
]
