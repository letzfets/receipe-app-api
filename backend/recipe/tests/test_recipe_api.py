"""
Test for recipe API
"""
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe

from recipe.serializers import (
    RecipeSerializer,
    RecipeDetailSerializer,
)


RECIPES_URL = reverse("recipe:recipe-list")


# needs to be afunction to be able to pass in the recipe_id:
def detail_url(recipe_id):
    """Create and return a recipe detail URL."""
    return reverse("recipe:recipe-detail", args=[recipe_id])


# Creating a function to use a sample recipe for various tests:
def create_recipe(user, **params):
    """Create and return a sample recipe"""
    defaults = {
        "title": "Sample recipe title",
        "time_minutes": 22,
        "price": Decimal("5.25"),
        "description": "Sample recipe description",
        "link": "https://www.example.com/recipe.pdf",
    }
    # If params get passed in, those will override the defaults:
    defaults.update(params)

    recipe = Recipe.objects.create(user=user, **defaults)
    return recipe


class PublicRecipeAPITests(TestCase):
    """Test unauthenticated recipe API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API."""
        res = self.client.get(reverse("recipe:recipe-list"))

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateRecipeAPITests(TestCase):
    """Test authenticated recipe API requests."""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            password="testpass123",
        )

        self.client.force_authenticate(user=self.user)

    # Creates two recipes, stores them in the database, and returns them:
    def test_retrieve_recipes(self):
        """Test retrieving a list of recipes."""
        # Creates two recipes in the database:
        create_recipe(user=self.user)
        create_recipe(user=self.user)

        res = self.client.get(RECIPES_URL)

        # Retrieve all recipes from the database in reverse order
        # most recent one has highest id, and is on top of the list:
        recipes = Recipe.objects.all().order_by("-id")
        # many = True tells serializer to return list of items - not only one:
        serializer = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    # Make sure, that the recipes from another user don't get returned:
    def test_recipes_limited_to_user(self):
        """Test retrieving recipes for user."""
        other_user = get_user_model().objects.create_user(
            email="other@example.com",
            password="password123",
        )
        # Creates one recipe for the other user:
        create_recipe(user=other_user)
        # and one for the authenticated user:
        create_recipe(user=self.user)

        res = self.client.get(RECIPES_URL)

        recipes = Recipe.objects.filter(user=self.user)
        serializer = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data, serializer.data)

    def test_get_recipe_detail(self):
        """Test viewing a recipe detail."""
        recipe = create_recipe(user=self.user)

        # Generate the URL for the detail view:
        url = detail_url(recipe.id)
        res = self.client.get(url)

        serializer = RecipeDetailSerializer(recipe)

        self.assertEqual(res.data, serializer.data)
