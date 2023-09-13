"""
URL mappings for the user API.
"""
from django.urls import path

from user import views

# is used by reverse function in tests/test_user_api.py:
app_name = "user"

urlpatterns = [
    path("create/", views.CreateUserView.as_view(), name="create"),
]
