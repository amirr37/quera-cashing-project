from rest_framework import serializers
from django.contrib.auth import get_user_model

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

    def validate(self, data):
        """
        Ensure that the 'password' field is present and not empty.
        """
        if 'password' not in data:
            raise serializers.ValidationError("Password is required.")
        if not data['password']:
            raise serializers.ValidationError("Password cannot be empty.")
        return data

    def create(self, validated_data):
        """
        Override the create method to set the password securely.
        """
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user