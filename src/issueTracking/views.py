from itertools import chain
from rest_framework import generics
from . import models
from . import serializers


class ProjectList(generics.ListCreateAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class UserList(generics.ListCreateAPIView):
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        project = models.Project.objects.get(id=self.kwargs['pk'])
        author = project.author
        contributorsUser = models.User.objects.filter(contributor__project=project).values()
        return chain([author], contributorsUser)
