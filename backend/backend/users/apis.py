from django.http import Http404
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.users.selectors import user_get
from backend.users.services import UserManager

class UserDetailApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        email = serializers.CharField()

    def get(self, request, user_id):
        user = user_get(user_id)

        if user is None:
            raise Http404

        data = self.OutputSerializer(user).data

        return Response(data)

class UserCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = UserManager.create_user(
            **serializer.validated_data
        )

        # Note: This shows a possible reusability for serializers between APIs
        # Usually, this is how we approach things, when building APIs at first
        # But at the very moment when we need to make a change to the output,
        # that's specific to this API, we'll introduce a separate OutputSerializer just for this API
        data = UserDetailApi.OutputSerializer(user).data

        return Response(data)
