from rest_framework import serializers
from . import models


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Project


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['user']
        model = models.Contributor


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Issue
