from rest_framework import permissions

from .models import Invoice, Request


# Permissions for Request

class IsNewRequest(permissions.BasePermission):
    """
    Check if Request have status NEW
    """

    def has_object_permission(self, request, view, obj):
        return obj.status is Request.NEW


# Permissions for Invoice

class IsUnpaidInvoice(permissions.BasePermission):
    """
    Check if Invoice have status NEW
    """

    def has_object_permission(self, request, view, obj):
        return obj.status is Invoice.UNPAID
