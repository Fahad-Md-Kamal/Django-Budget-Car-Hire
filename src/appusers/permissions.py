from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Handles permission to the data
    """
    MY_SAFE_METHODS = [permissions.SAFE_METHODS, permissions.IsAdminUser]

    def has_object_permission(self, request, view, obj):
        """ 
        If the user is owner of the data 
        """
        if request.method in self.MY_SAFE_METHODS:
            return True

        return request.user == obj.user.id
        