# Generated by Django 5.0.2 on 2024-02-07 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_product_manufactured_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='manufactured_at',
            field=models.DateTimeField(default='', verbose_name='дата производства'),
        ),
    ]
