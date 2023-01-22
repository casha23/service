from rest_framework import permissions

from .models import Request


class IsNewRequest(permissions.BasePermission):
    """
    Check if request have status NEW
    """

    def has_object_permission(self, request, view, obj):
        return obj.status is Request.NEW
