from django.conf import settings
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .serializers import CustomUserSerializer

import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')


# todo : config django settings module
class CustomUserCreateAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testuserssssddsd',
            'password': 'testpassword'
        }

    def test_create_user_success(self):
        # Send a POST request to the view's endpoint
        response = self.client.post('http://127.0.0.1:8000/account/create-user/', self.user_data, format='json')
        user_id = response.json().get('id')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_with_invalid_data(self):
        invalid_user_data = {'username': 'testuser'}
        response = self.client.post('http://127.0.0.1:8000/account/create-user/', invalid_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


