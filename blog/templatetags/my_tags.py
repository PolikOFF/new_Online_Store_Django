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
    return '#'