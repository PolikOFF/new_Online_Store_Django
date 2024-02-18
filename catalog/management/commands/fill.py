import json

from django.core.management import BaseCommand
import os

from catalog.models import Category, Product


class Command(BaseCommand):
    """Класс для создания команды, наследуемый от базового класса BaseCommand."""

    @staticmethod
    def json_read():
        """Статический метод для считывания данных из .json файла."""
        with open(os.path.join('catalog_data.json'), 'r', encoding='utf-16') as f:
            data_file = json.load(f)
            return data_file

    def handle(self, *args, **kwargs):
        """
        Обязательный метод для реализации команды.
        Команда умеет заполнять базу данных,
        при этом предварительно зачищая ее от старых данных.
        """
        product_for_create = []
        category_for_create = []

        for category in Command.json_read():
            if category['model'] == "catalog.category":
                category_for_create.append(
                    Category(pk=category['pk'], name=category['fields']['name'],
                             description=category['fields']['description'])
                )
        Category.objects.all().delete()
        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read():
            if product['model'] == "catalog.product":
                product_for_create.append(
                    Product(
                        pk=product['pk'],
                        name=product['fields']['name'],
                        description=product['fields']['description'],
                        image=product['fields']['image'],
                        category=Category.objects.get(pk=product['fields']['category']),
                        price=product['fields']['price'],
                        created_at=product['fields']['created_at'],
                        updated_at=product['fields']['updated_at']
                    )
                )

        Product.objects.all().delete()
        Product.objects.bulk_create(product_for_create)
