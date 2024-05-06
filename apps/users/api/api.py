from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.api.serializers import UserSerializer
from apps.users.models import User


class UserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data)
    