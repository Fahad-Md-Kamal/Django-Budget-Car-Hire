from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom Permission to only allow owners of an object to edit it
    """
    def has_object_permission(self, request, view, obj):

        # SAFE_METHODS = [permissions.SAFE_METHODS, permissions.IsAdminUser]

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user