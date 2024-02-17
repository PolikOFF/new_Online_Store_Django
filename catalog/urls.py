from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import categories, contacts, category, product_info, product_details

app_name = CatalogConfig.name

urlpatterns = [
    path('', categories, name='categories'),
    path('contacts/', contacts),
    path('category/', category, name='category'),
    path('<int:pk>/product_info/', product_info, name='product_info'),
    path('<int:pk>/product_details/', product_details, name='product_details'),
]
