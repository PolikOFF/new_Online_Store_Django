from django.contrib import admin

from catalog.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс для регистрации продукта в административной панели."""
    list_display = ('pk', 'name', 'price', 'category')
    list_filter = ['category']
    search_fields = ('name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Класс для регистрации категории в административной панели."""
    list_display = ('pk', 'name')
