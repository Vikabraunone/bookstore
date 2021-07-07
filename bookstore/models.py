from django.db import models


# Create your models here.
class BookShop(models.Model):
    city = models.CharField(
        max_length=30,
        verbose_name='Город',
    )
    street = models.CharField(
        max_length=100,
        verbose_name='Улица',
    )

    def __str__(self):
        return f'{self.city} {self.street}'

    class Meta:
        verbose_name = 'Книжный магазин'
        verbose_name_plural = 'Книжные магазины'


class Book(models.Model):
    shop = models.ForeignKey('BookShop', on_delete=models.PROTECT, null=True)
    title = models.CharField(
        max_length=100,
        verbose_name='Название',
    )
    author = models.CharField(
        max_length=100,
        verbose_name='Автор',
    )
    description = models.CharField(
        max_length=500,
        blank=True,
        verbose_name='Описание',
    )
    publishing_house = models.CharField(
        max_length=20,
        verbose_name='Издательство',
    )
    number_of_pages = models.PositiveIntegerField(
        verbose_name='Количество страниц',
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title
