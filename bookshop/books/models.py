from django.db import models


class Tag(models.Model):
    name = models.CharField(verbose_name='標籤名稱', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '標籤'
        verbose_name_plural = '標籤'


class Category(models.Model):
    name = models.CharField(verbose_name='分類名稱', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分類'
        verbose_name_plural = '分類'


class Book(models.Model):
    def __str__(self):
        return self.name

    # general fields
    name = models.CharField(verbose_name='名稱', max_length=255)
    description = models.TextField(
        verbose_name='內容簡介',
        default='',
        blank=True
    )
    original_price = models.PositiveIntegerField(verbose_name='原價', default=0)
    price = models.PositiveIntegerField(verbose_name='售價', default=0)
    category = models.ForeignKey(
        Category,
        verbose_name='分類',
        null=True,
        blank=True
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='標籤',
        blank=True
    )

    # status and time related fields
    STATUS_CHOICES = (
        (0, '未上架'),
        (1, '上架中'),
        (2, '已下架')
    )
    status = models.PositiveSmallIntegerField(
        verbose_name='狀態',
        choices=STATUS_CHOICES,
        default=0
    )
    created = models.DateTimeField(verbose_name='新增時間', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='更新時間', auto_now=True)
    published = models.DateTimeField(verbose_name='上架時間', null=True)

    # book related fields
    author = models.CharField(
        verbose_name='作者',
        max_length=100,
        default='',
        blank=True
    )
    translator = models.CharField(
        verbose_name='譯者',
        max_length=100,
        default='',
        blank=True
    )
    publisher = models.CharField(
        verbose_name='出版社',
        max_length=100,
        default='',
        blank=True
    )
    isbn = models.CharField(
        verbose_name='ISBN',
        max_length=13,
        default='',
        blank=True
    )
    language = models.CharField(
        verbose_name='語言',
        max_length=20,
        default='',
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '書籍'
        verbose_name_plural = '書籍'
