from django.db import models


class Workflow(models.Model):
    title = models.CharField(max_length=200)


class GcpServiceAccount(models.Model):
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
