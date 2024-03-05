from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Category, Product


class CategoriesListView(ListView):
    """Класс для вывода всех категорий продуктов"""
    model = Category


class ContactsView(TemplateView):
    """Класс для вывода страницы с контактами"""
    template_name = 'catalog/contacts.html'


class ProductListView(ListView):
    """Класс для вывода всех продуктов определенной категории"""
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset


class ProductDetailView(DetailView):
    """Класс для вывода информации о продукте по его pk"""
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:category_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:category_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:category_list')
