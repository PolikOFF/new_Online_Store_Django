# Generated by Django 5.0.2 on 2024-02-25 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('content', models.TextField(verbose_name='содержимое')),
                ('create_at', models.DateField(blank=True, null=True, verbose_name='дата создания')),
                ('view_count', models.IntegerField(default=0, verbose_name='счетчик просмотров')),
                ('is_published', models.BooleanField(default=True, verbose_name='признак публикации')),
                ('image', models.ImageField(upload_to='', verbose_name='изображение превью')),
                ('slug', models.CharField(max_length=150, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
    ]
