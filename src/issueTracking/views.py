from rest_framework import generics
from . import models
from . import serializers


class ProjectsList(generics.ListCreateAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectsSerializer
