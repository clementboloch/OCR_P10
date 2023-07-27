from rest_framework import permissions
from .models import Contributor


class IsContributor(permissions.BasePermission):
    """
    Custom permission to only allow contributors of a project to access it.
    """

    def has_object_permission(self, request, view, obj):
        # Only allow the contributor of the project to access it.
        # Check if a Contributor instance exists with the user as user and the project as project.
        return Contributor.objects.filter(user=request.user, project=obj).exists()


class IsAuthor(permissions.BasePermission):
    """
    Custom permission to only allow authors of a ressource to access it.
    """

    def has_object_permission(self, request, view, obj):
        # Only allow the author of the ressource to access it.
        # Check if the author of the ressource is the user.
        return obj.author == request.user
