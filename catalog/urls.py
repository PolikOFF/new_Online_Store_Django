from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CategoriesListView, ContactsView, ProductListView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoriesListView.as_view(), name='category_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('category/', CategoriesListView.as_view(), name='category'),
    path('<int:pk>/list_of_category_products/', ProductListView.as_view(), name='list_of_category_products'),
    path('<int:pk>/product_detail/', ProductDetailView.as_view(), name='product_detail'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/product_update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/product_delete/', ProductDeleteView.as_view(), name='product_delete'),
]
