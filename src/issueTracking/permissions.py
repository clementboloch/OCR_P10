from rest_framework import permissions
from .models import Contributor


class HasPermission(permissions.BasePermission):
    """
    Custom permission to only allow users with the permission to access the ressource.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return Contributor.objects.filter(user=request.user, project=obj).exists()
        else:
            return obj.author == request.user
