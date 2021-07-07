from django_filters import rest_framework as filters
from .models import BookShop
from .models import Book


class BookShopFilter(filters.FilterSet):
    class Meta:
        model = BookShop
        fields = ['city']


class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publishing_house']