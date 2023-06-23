from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Project


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['first_name', 'last_name', 'email']
        model = User


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['user']
        model = models.Contributor


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Issue
