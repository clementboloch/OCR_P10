from itertools import chain
from django.shortcuts import get_object_or_404
from rest_framework import generics
from . import models
from . import serializers
from account.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsContributor


class ProjectList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsContributor,)

    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class UserList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsContributor,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer
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
    permission_classes = (IsAuthenticated, IsContributor,)

    queryset = models.Contributor.objects.all()
    serializer_class = serializers.ContributorSerializer

    def get_object(self, queryset=None):
        project_id = self.kwargs.get('project_id')
        user_id = self.kwargs.get('user_id')
        contributor = get_object_or_404(self.queryset, project_id=project_id, user_id=user_id)
        return contributor


class IssueList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsContributor,)

    serializer_class = serializers.IssueSerializer

    def get_queryset(self):
        project = models.Project.objects.get(id=self.kwargs['pk'])
        return models.Issue.objects.filter(project=project)

    def perform_create(self, serializer):
        project = models.Project.objects.get(id=self.kwargs['pk'])
        serializer.save(project=project)
