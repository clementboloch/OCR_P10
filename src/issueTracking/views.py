# from itertools import chain
from itertools import chain
from django.shortcuts import get_object_or_404
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
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.UserSerializer
        return serializers.ContributorSerializer

    def get_queryset(self):
        project = models.Project.objects.get(id=self.kwargs['pk'])
        author = project.author
        contributorsUser = models.User.objects.filter(contributor__project=project).values()
        return chain([author], contributorsUser)

    def perform_create(self, serializer):
        project_id = self.kwargs['pk']
        project = models.Project.objects.get(id=project_id)
        serializer.save(project=project)


class ContributorDelete(generics.DestroyAPIView):
    queryset = models.Contributor.objects.all()
    serializer_class = serializers.ContributorSerializer

    def get_object(self, queryset=None):
        project_id = self.kwargs.get('project_id')
        user_id = self.kwargs.get('user_id')
        contributor = get_object_or_404(self.queryset, project_id=project_id, user_id=user_id)
        return contributor
