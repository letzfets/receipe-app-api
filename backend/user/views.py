"""
Views for the user API.
"""
from rest_framework import generics
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
