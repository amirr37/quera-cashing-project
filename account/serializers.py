from rest_framework import serializers
from django.contrib.auth import get_user_model


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # This ensures the correct user model is used
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'phone_number')