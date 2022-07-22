from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Book, Human

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = '__all__'