from django.contrib import admin
from .models import Book
from .models import BookShop


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'shop', 'description', 'publishing_house', 'number_of_pages')
    list_display_links = ('id', 'title', 'author', 'shop')
    search_fields = ('id', 'title', 'author', 'shop', 'description', 'publishing_house')


class BookshopAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'street')
    list_display_links = ('id', 'city', 'street')
    search_fields = ('id', 'city', 'street')


admin.site.register(Book, BookAdmin)
admin.site.register(BookShop, BookshopAdmin)
