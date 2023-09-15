"""
Views for the user API.
"""
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)


# CreateAPIView: handles an HTTP POST request to the URL
class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""

    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""

    # To enable the view in the browsable API:
    serializer_class = AuthTokenSerializer
    # To enable the view in the browsable API:
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""

    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # Overrides the get_object() function in RetrieveUpdateAPIView
    def get_object(self):
        """Retrieve and return authentication user."""
        # When the user is authenticated, the authentication system
        # will assign the user to the request object
        # runs it also through serializer before returning it
        return self.request.user
