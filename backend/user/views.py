"""
Views for the user API.
"""
from rest_framework import generics

from user.serializers import UserSerializer


# CreateAPIView: handles an HTTP POST request to the URL
class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""

    serializer_class = UserSerializer
