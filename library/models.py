from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)


class Human(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
