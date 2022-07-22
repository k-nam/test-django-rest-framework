from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Workflow, GcpServiceAccount

class WorkflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workflow
        fields = '__all__'


class GcpServiceAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = GcpServiceAccount
        fields = '__all__'