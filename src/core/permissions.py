from rest_framework import permissions

class IsProfileOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom Permission to only allow owners of an object to edit it
    """
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user
    

class IsDataOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom Permission to only allow owners of an object to edit it
    """
    def has_object_permission(self, request, view, obj):


        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user or request.user.is_staff
    