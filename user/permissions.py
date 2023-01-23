from rest_framework import permissions


class IsMasterUser(permissions.BasePermission):
    """
    Check if user is a master
    """

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.is_master
