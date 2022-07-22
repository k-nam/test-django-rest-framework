from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Workflow, GcpServiceAccount


class GcpServiceAccountSerializer(serializers.ModelSerializer):
    # workflow = WorkflowSerializer()
    class Meta:
        model = GcpServiceAccount
        fields = '__all__'

class WorkflowSerializer(serializers.ModelSerializer):
    gcp_service_accounts = GcpServiceAccountSerializer(many=True, read_only=True)


    # gcp_service_account = GcpServiceAccountSerializer(queryset=GcpServiceAccount.objects.filter())
    class Meta:
        model = Workflow
        fields = '__all__'