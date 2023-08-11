from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from . import models
from . import serializers
from account.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import HasPermission, IsContributor
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
        serializer.save(author=self.request.user)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, HasPermission,)

    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer

    serializer_class_post = serializers.ProjectCreateSerializer

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return super().get_serializer_class()
        else:
            return self.serializer_class_post


class ContributorList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, HasPermission,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer
        return serializers.ContributorSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        project = get_object_or_404(models.Project, id=project_id)
        contributorsUser = User.objects.filter(contributor__project=project).values()
        return contributorsUser

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_id')
        project = get_object_or_404(models.Project, id=project_id)
        self.check_object_permissions(self.request, project)
        serializer.save(project=project)


class ContributorDelete(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, HasPermission,)

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
    serializer_class_post = serializers.IssueCreateSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return self.serializer_class_post
        return super().get_serializer_class()

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        project = get_object_or_404(models.Project, id=project_id)
        self.check_object_permissions(self.request, project)
        return models.Issue.objects.filter(project=project)

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_id')
        project = get_object_or_404(models.Project, id=project_id)
        self.check_object_permissions(self.request, project)
        serializer.save(project=project, author=self.request.user)


class IssueUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, HasPermission,)

    queryset = models.Issue.objects.all()
    serializer_class = serializers.IssueSerializer
    serializer_class_put = serializers.IssueCreateSerializer

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return self.serializer_class_put
        return super().get_serializer_class()

    def get_object(self, queryset=None):
        project_id = self.kwargs.get('project_id')
        project = get_object_or_404(models.Project, id=project_id)
        issue_id = self.kwargs.get('issue_id')
        issue = get_object_or_404(self.queryset, project_id=project_id, id=issue_id)
        if self.request.method in permissions.SAFE_METHODS:
            obj = project
        else:
            obj = issue
        self.check_object_permissions(self.request, obj)
        return issue


class CommentList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsContributor,)

    serializer_class = serializers.CommentSerializer
    serializer_class_post = serializers.CommentCreateSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return self.serializer_class_post
        return super().get_serializer_class()

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        project = get_object_or_404(models.Project, id=project_id)
        self.check_object_permissions(self.request, project)
        issue = models.Issue.objects.get(id=self.kwargs['issue_id'])
        return models.Comment.objects.filter(project=project, issue=issue)

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_id')
        project = get_object_or_404(models.Project, id=project_id)
        issue = models.Issue.objects.get(id=self.kwargs['issue_id'])
        self.check_object_permissions(self.request, project)
        serializer.save(project=project, author=self.request.user, issue=issue)


class CommentUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, HasPermission,)

    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    serializer_class_put = serializers.CommentCreateSerializer

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return self.serializer_class_put
        return super().get_serializer_class()

    def get_object(self, queryset=None):
        project_id = self.kwargs.get('project_id')
        project = get_object_or_404(models.Project, id=project_id)
        issue_id = self.kwargs.get('issue_id')
        comment_id = self.kwargs.get('comment_id')
        comment = get_object_or_404(self.queryset, project_id=project_id, issue_id=issue_id, id=comment_id)
        if self.request.method in permissions.SAFE_METHODS:
            obj = project
        else:
            obj = comment
        self.check_object_permissions(self.request, obj)
        return comment
