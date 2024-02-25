from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """Класс для регистрации продукта в административной панели."""
    list_display = ('title', 'create_at', 'view_count', 'is_published', 'slug')
    list_filter = ['create_at']
    search_fields = ['title']
