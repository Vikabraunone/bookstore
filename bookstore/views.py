from .models import Book
from .models import BookShop
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from .serializers import BookSerializer
from .serializers import BookShopSerializer
from .service import BookShopFilter, BookFilter


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookFilter


class BookShopViewSet(viewsets.ModelViewSet):
    queryset = BookShop.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BookShopSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookShopFilter
