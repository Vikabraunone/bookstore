from rest_framework import serializers
from .models import Book
from .models import BookShop


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookShop
        fields = '__all__'