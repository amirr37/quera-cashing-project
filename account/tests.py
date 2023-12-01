from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .serializers import CustomUserSerializer


# todo : config django settings module
class CustomUserCreateAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }

    def test_create_user_success(self):
        # Send a POST request to the view's endpoint
        response = self.client.post('http://127.0.0.1:8000/auth-token', self.user_data, format='json')

        # Assert that the response has a 201 Created status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the user object was created in the database
        self.assertTrue(get_user_model().objects.filter(username='testuser').exists())

        # Add more assertions based on your expected response data
        # For example, you might want to check if the response contains the created user's data
        user_id = response.json().get('id')
        self.assertIsNotNone(user_id)
        self.assertEqual(response.json().get('username'), 'testuser')
        self.assertEqual(response.json().get('email'), 'testuser@example.com')

    # Add more test cases if needed
