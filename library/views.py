from rest_framework import viewsets, permissions
from library.models import Book, Human
from library.serializers import BookSerializer, HumanSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class HumanViewSet(viewsets.ModelViewSet):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer
    permission_classes = [permissions.IsAuthenticated]