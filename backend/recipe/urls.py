"""
URL mapping for recipe app.
"""

from django.urls import (
    path,
    include,
)
from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
# creates a new endpoint under /api/recipe
# registers all views of the viewset to the recipe endpoint and
# as it's a ModelViewset, it automatically creates all available
# methods for Create, Read, Update and Delete through the HTTP methods
# GET, POST, PUT, PATCH & DELETE
router.register("recipes", views.RecipeViewSet)

# name used for reverse lookup patterns in test:
app_name = "recipe"

urlpatterns = [
    path("", include(router.urls)),
]
