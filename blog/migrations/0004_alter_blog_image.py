# Generated by Django 5.0.2 on 2024-02-29 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_image_alter_blog_view_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images', verbose_name='изображение превью'),
        ),
    ]