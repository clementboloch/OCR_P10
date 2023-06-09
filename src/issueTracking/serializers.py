from rest_framework import serializers
from . import models


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Project
