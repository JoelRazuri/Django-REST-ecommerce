from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'last_name', 'image', 'is_superuser', 'is_staff']