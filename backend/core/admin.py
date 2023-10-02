"""
Django admin customization
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# allows for translation of text:
# https://docs.djangoproject.com/en/3.2/topics/i18n/translation/#module-django.utils.translation
# (underscore is used as shortcut for gettext_lazy)
from django.utils.translation import gettext_lazy as _
from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users"""

    ordering = ["id"]
    list_display = ["email", "name"]
    # only access the fields, that are present in customized user model:
    # overrides the default fields, which include:
    # date_joined, username, first_name, last_name
    # but those are not used in the customized user model.
    fieldsets = (
        # "None" stands for title
        (None, {"fields": ("email", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (
            _("Important dates"),
            {"fields": ("last_login",)},
        ),
    )
    readonly_fields = ["last_login"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Recipe)
