from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class BaseTest(APITestCase):
    """Base test class to use across multiple test files."""

    def setUp(self):
        self.client = APIClient()

        # Create a superuser
        self.superuser = User.objects.create_superuser(
            first_name="Test",
            last_name="Admin",
            email="admin@test.com",
            password="testpass123",
        )

        # Generate JWT token via simplejwt
        refresh = RefreshToken.for_user(self.superuser)
        self.access_token = str(refresh.access_token)

        # Set token for authenticated requests
        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer " + self.access_token,
        )
