"""
Tests for the Django admin modifications.
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Test for Django admin"""

    # unit-test module for Python uses camelCase
    # whereas normal convention is snake_case
    def setUp(self):
        """Create User and client."""
        self.client = Client()
        # create a superuser
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@example.com", password="test123"
        )
        # login with the superuser
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            password="test123",
            name="Test user",
        )

    def test_users_list(self):
        """Test that users are listed on user page."""
        # generate url for list user page
        url = reverse("admin:core_user_changelist")
        # perform http get request
        res = self.client.get(url)

        # assertContains checks that the response contains a certain item
        # and also checks that the http response is 200
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """Test that the edit user page works."""
        url = reverse("admin:core_user_change", args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
