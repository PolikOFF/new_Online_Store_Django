from django.contrib import admin

from catalog.models import Product, Category, Version


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


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('version_name', 'version_number', 'is_current', 'product')
    list_filter = ['is_current']
    search_fields = ('version_name',)
