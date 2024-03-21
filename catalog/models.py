from django.conf import settings
from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    """
    Модель для продукта относящегося к категории по ключу ForeignKey.
    :param name: Название продукта.
    :param description - не обязательное поле: Описание модели продукта.
    :param image - не обязательное поле: Медиафайл для отображения продукта.
    :param category: Является ключом ForeignKey для модели Category.
    :param price - не обязательное поле: Цена продукта.
    :param created_at: Дата создания продукта.
    :param updated_at: Дата последнего изменения в базе данных.
    """
    name = models.CharField(max_length=150, verbose_name='продукт')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='цена', **NULLABLE)
    created_at = models.DateTimeField(verbose_name='дата создания записи в БД', **NULLABLE)
    updated_at = models.DateTimeField(verbose_name='дата последнего изменения записи в БД', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='владелец', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='опубликован')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            (
                'set_published', 'Can publish product'
            ),
            (
                'change_description', 'Can change product description'
            ),
            (
                'change_category', 'Can change category'
            ),
        ]

    def __str__(self):
        return f"{self.name} ({self.category})"


class Category(models.Model):
    """
    Модель для категории продукта.
    :param name: Название категории продукта,
    :param description: Описание категории продукта.
    """
    name = models.CharField(max_length=150, verbose_name='категория')
    description = models.CharField(max_length=300, verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Version(models.Model):
    """Модель для версии продукта"""
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    version_number = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='имя версии')
    is_current = models.BooleanField(verbose_name='текущая версия')

    def __str__(self):
        return f'Продукт - {self.product}, версия - {self.version_name}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
