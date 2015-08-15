from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has a 'user' attribute.
    """

    def has_object_permission(self, request, view, obj):

        # Instance must have an attribute named `owner`.
        return obj.user == request.user

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True


        try: #obj is Review or Tip
            return obj.author == request.user
        except: #obj is Favorite
            return obj.user == request.user