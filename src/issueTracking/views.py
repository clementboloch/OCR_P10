from django.shortcuts import get_object_or_404
from rest_framework import generics
from . import models
from . import serializers
from account.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsContributor, IsAuthor
from account.models import UserData as User


class ProjectList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    serializer_class_post = serializers.ProjectCreateSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return self.serializer_class_post
        return super().get_serializer_class()

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(author=self.request.user)


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
        self.check_object_permissions(self.request, project)
        contributorsUser = User.objects.filter(contributor__project=project).values()
        return contributorsUser

    def perform_create(self, serializer):
        project_id = self.kwargs['pk']
        project = models.Project.objects.get(id=project_id)
        serializer.save(project=project)


class ContributorDelete(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, IsContributor, IsAuthor,)

    queryset = models.Contributor.objects.all()
    serializer_class = serializers.ContributorSerializer

    def get_object(self, queryset=None):
        project_id = self.kwargs.get('project_id')
        project = get_object_or_404(models.Project, id=project_id)
        self.check_object_permissions(self.request, project)
        user_id = self.kwargs.get('user_id')
        contributor = get_object_or_404(self.queryset, project_id=project_id, user_id=user_id)
        return contributor


class IssueList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsContributor,)

    serializer_class = serializers.IssueSerializer

    def get_queryset(self):
        project = models.Project.objects.get(id=self.kwargs['pk'])
        self.check_object_permissions(self.request, project)
        return models.Issue.objects.filter(project=project)

    def perform_create(self, serializer):
        project = models.Project.objects.get(id=self.kwargs['pk'])
        serializer.save(project=project)
