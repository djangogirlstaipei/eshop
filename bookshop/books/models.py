from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    # general fields
    name = models.CharField(max_length=255)
    description = models.TextField(
        default='',
        blank=True
    )
    original_price = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True
    )

    # status and time related fields
    STATUS_CHOICES = (
        (0, '未上架'),
        (1, '上架中'),
        (2, '已下架')
    )
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES,
        default=0
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(null=True)

    # book related fields
    author = models.CharField(
        max_length=100,
        default='',
        blank=True
    )
    translator = models.CharField(
        max_length=100,
        default='',
        blank=True
    )
    publisher = models.CharField(
        max_length=100,
        default='',
        blank=True
    )
    isbn = models.CharField(
        max_length=13,
        default='',
        blank=True
    )
    language = models.CharField(
        max_length=20,
        default='',
        blank=True
    )
