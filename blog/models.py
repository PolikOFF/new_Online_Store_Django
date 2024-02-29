from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    """
    Модель для записи блога.
    :param title: Заголовок.
    :param content: Содержимое.
    :param create_at: Дата создания.
    :param view_count: Количество просмотров.
    :param is_published: Признак публикации.
    :param image: Превью(изображение).
    :param slug: Человеко понятный URL.
    """
    title = models.CharField(max_length=150, verbose_name="заголовок")
    content = models.TextField(verbose_name='содержимое')
    create_at = models.DateField('дата создания', **NULLABLE)
    view_count = models.IntegerField(default=0, verbose_name='счетчик просмотров', **NULLABLE)
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')
    image = models.ImageField(upload_to='static/images', verbose_name='изображение превью', **NULLABLE)
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
