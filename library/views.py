from rest_framework import viewsets, permissions
from library.models import Workflow, GcpServiceAccount
from library.serializers import WorkflowSerializer, GcpServiceAccountSerializer


class WorkflowViewSet(viewsets.ModelViewSet):
    queryset = Workflow.objects.all().order_by('title')
    serializer_class = WorkflowSerializer
    permission_classes = [permissions.IsAuthenticated]


class GcpServiceAccountViewSet(viewsets.ModelViewSet):
    queryset = GcpServiceAccount.objects.all()
    serializer_class = GcpServiceAccountSerializer
    permission_classes = [permissions.IsAuthenticated]