# Generated by Django 5.0.2 on 2024-02-07 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='salary',
            new_name='price',
        ),
    ]