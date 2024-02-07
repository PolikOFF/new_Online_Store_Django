from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='продукт')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    salary = models.IntegerField(verbose_name='цена', **NULLABLE)
    manufactured_at = models.DateTimeField(verbose_name='дата производства', default="")
    created_at = models.DateTimeField(verbose_name='дата создания записи в БД')
    updated_at = models.DateTimeField(verbose_name='дата последнего изменения записи в БД')

    def __str__(self):
        return f"{self.name} ({self.category}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='категория')
    description = models.CharField(max_length=300, verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
