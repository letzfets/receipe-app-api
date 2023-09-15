"""
Serializers for user API view.
"""
from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.utils.translation import gettext as _

from rest_framework import serializers


# A serializer takes a JSON input, that is posted to the API,
# validates the input to make sure that it is secure and correct
# as part of validation rules, and then it converts it either
# a Python object or a model that is then saved to the database.
#
# Different base classes: serializers.Serializer or serializers.ModelSerializer
# - ModelSerializer: automatically validate and save fields based on the model
# that is defined in serializer.
class UserSerializer(serializers.ModelSerializer):
    """Serializer for user object."""

    # Here we tell Django REST framework the model and fields that we
    # want to pass serializer needs to know, which model it is representing:
    class Meta:
        model = get_user_model()
        # Fields that are required from the user to be able to create
        # a new user but not fields like is_active, is_staff or is_superuser
        # as the user is not allowed to set those fields.
        fields = ("email", "password", "name")
        # Extra keyword args (kwargs) for configuration:
        # Make password write only,
        # i.e. user can set it but the API does not return it
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    # Overrides standard behavior of Serializer's create() function
    # is user would send password in plain text, it would be saved
    # as plain text, but we want to use the encryption throgh the
    # create_user method provided in the Model Manager.
    # This method is called after validation and only if validation is successful.
    # Validation error: could be minimum length of password.
    def create(self, validated_data):
        """Create and return a new user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for user auth token."""

    email = serializers.EmailField()
    password = serializers.CharField(
        # mainly for the browsable API, aka /api/docs:
        style={"input_type": "password"},
        # password could contain spaces - django would trim them by default:
        trim_whitespace=False,
    )

    # view calls validation function when it passes data to serializer
    def validate(self, attrs):
        """Validate and authenticate the user."""
        email = attrs.get("email")
        password = attrs.get("password")
        # authenticate function comes built-in with Django
        # returns user object is password is correct
        # otherwise returns None
        user = authenticate(
            # contains header from request,
            # request is a required field
            request=self.context.get("request"),
            username=email,
            password=password,
        )
        if not user:
            msg = _("Unable to authenticate with provided credentials")
            # standard way of raising validation error in serializer
            # view turns this into a 400 response
            raise serializers.ValidationError(msg, code="authentication")

        attrs["user"] = user
        return attrs
