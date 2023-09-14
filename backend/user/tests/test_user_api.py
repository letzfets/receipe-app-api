"""
Tests for user API.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse("user:create")
TOKEN_URL = reverse("user:token")


def create_user(**params):
    """Helper function to create and return a new user."""
    return get_user_model().objects.create_user(**params)


# Public and private user API tests:
# - Public tests don't require a user login, like
#   creating a new user or logging in.
# - Private tests require a user login
# Two different test classes for public and private


class PublicUserAPITests(TestCase):
    """Test the public features of users API."""

    # Creates and API client for testing:
    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        """Test creating user is successful."""
        payload = {
            "email": "test@example.com",
            "password": "testpass123",
            "name": "Test Name",
        }
        res = self.client.post(CREATE_USER_URL, payload)

        # Assert that the response status code is 201:
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload["email"])
        # Assert that the password is correctly hashed:
        self.assertTrue(user.check_password(payload["password"]))
        # Assert that the password is not returned in the response:
        self.assertNotIn("password", res.data)

    def test_user_already_exists(self):
        """Test error returned if user with email exists."""
        payload = {
            "email": "test@example.com",
            "password": "testpass123",
            "name": "Test Name",
        }
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        # Assert that the response status code is 400:
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that error is returned if password is less than 5 characters"""
        payload = {
            "email": "test@example.com",
            "password": "pw",
            "name": "Test Name",
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(email=payload["email"]).exists()
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        """Test generates token for valid credentials."""
        user_details = {
            "name": "Test Name",
            "email": "test@example.com",
            "password": "test-user-pass123",
        }
        create_user(**user_details)

        payload = {"email": user_details["email"], "password": user_details["password"]}

        res = self.client.post(TOKEN_URL, payload)

        self.assertIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        """Test returns error if credentials are invalid."""
        user_details = {
            "email": "test@example.com",
            "password": "goodpass",
        }
        create_user(**user_details)

        payload = {"email": user_details["email"], "password": "badpass"}

        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_blank_password(self):
        """Test returns error if password is blank."""
        payload = {"email": "test@example.com", "password": ""}

        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
