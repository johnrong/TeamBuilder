from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the snippet.
        return (obj.owner == request.user or request.user.is_staff)


class IsPublisherOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # print(request.method + " " + request.user.profile.role)
        if request.method == 'POST':
            if request.user.user_profile.role == 'special':
                return True
            else:
                return False
        else:
            return True
