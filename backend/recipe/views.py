"""
Views for the recipe APIs.
"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""

    serializer_class = serializers.RecipeSerializer
    # This queryset is managed by the this ModelViewSet:
    queryset = Recipe.objects.all()
    # support token authentication:
    authentication_classes = [TokenAuthentication]
    # user needs to be authenticated to use this API:
    permission_classes = [IsAuthenticated]

    # Override the get_queryset() function to return only the
    # recipes for the authenticated user:
    def get_queryset(self):
        """Return objects for the current authenticated user only."""
        # self.request.user is the authenticated user:
        return self.queryset.filter(user=self.request.user).order_by("-id")
