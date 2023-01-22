from rest_framework import permissions


class IsMasterUser(permissions.BasePermission):
    """
    Check if user is a master
    """

    def has_permission(self, request, view):
        return request.user.is_master
