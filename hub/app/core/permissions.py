from rest_framework import permissions


# Is owner or read only permission
# - - - - - - - - - - - - - - - - - - -
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return False
        # return request.user in obj.group.uuiduser_set


# Is creation or is authenticated
# - - - - - - - - - - - - - - - - - - -
class IsCreationOrIsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            if view.action == 'create':
                return True
            else:
                return False
        else:
            return True