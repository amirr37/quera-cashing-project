from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from account.serializers import CustomUserSerializer


# Create your views here.


class CustomUserCreateAPIView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        # Override the create method to customize the response if needed
        response = super().create(request, *args, **kwargs)
        # Add any additional logic here if needed
        return response