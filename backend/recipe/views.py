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

    # standard serializer is the detail serializer:
    # only for the list view, the list serializer is used
    # see get_serializer_class() below
    serializer_class = serializers.RecipeDetailSerializer
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

    # Override the get_serializer_class() to use the details serializer,
    # if user causes the details view:
    def get_serializer_class(self):
        """Return serializer class for the request."""
        if self.action == "list":
            # important don't call the serializer class with ()!
            # like serializers.RecipeDetailSerializer() because
            # get_serializer_class() expects an object of the class,
            # e.g. serializers.RecipeDetailSerializer.
            return serializers.RecipeSerializer

        return self.serializer_class
