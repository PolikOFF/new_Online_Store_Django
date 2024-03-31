from django import template

register = template.Library()


@register.filter()
def my_media(value):
    """
    Шаблонный фильтр, который принимает данные
    и добавляет к ним 'media' перед переданной строкой
    """
    if value:
        return f'/media/{value}'
    return '/static/images/product_plug.png'


@register.filter()
def version(product):
    """Шаблонный фильтр для отображения информации по версии продукта"""
    versions = product.version_set
    for version in versions:
        if version.is_current:
            return f'Активная версия - {version}.'
        return f'У продукта отсутствуют версии.'
