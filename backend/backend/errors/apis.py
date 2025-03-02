from rest_framework.response import Response
from rest_framework.views import APIView

from backend.api.exception_handlers import (
    drf_default_with_modifications_exception_handler,
    hacksoft_proposed_exception_handler,
)
from backend.errors.services import trigger_errors
from backend.users.services import UserManager


class TriggerErrorApi(APIView):
    def get(self, request):
        data = {
            "drf_default_with_modifications": trigger_errors(drf_default_with_modifications_exception_handler),
            "hacksoft_proposed": trigger_errors(hacksoft_proposed_exception_handler),
        }

        return Response(data)


class TriggerValidateUniqueErrorApi(APIView):
    def get(self, request):
        # Due to the fiddling with transactions, this example a different API
        UserManager.create_user(email="unique@hacksoft.io", password="user")
        UserManager.create_user(email="unique@hacksoft.io", password="user")

        return Response()


class TriggerUnhandledExceptionApi(APIView):
    def get(self, request):
        raise Exception("Oops")

        return Response()
