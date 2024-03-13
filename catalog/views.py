from django.core.exceptions import ObjectDoesNotExist
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Category, Product, Version


class CategoriesListView(ListView):
    """Класс для вывода всех категорий продуктов"""
    model = Category


class ContactsView(TemplateView):
    """Класс для вывода страницы с контактами"""
    template_name = 'catalog/contacts.html'


class ProductListView(ListView):
    """Класс для вывода всех продуктов определенной категории"""
    model = Product

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(category_id=self.kwargs.get('pk'))
    #     return queryset

    # def get_context_data(self, **kwargs):
    #
    #     context = super().get_context_data(**kwargs)
    #     products = self.get_queryset()
    #
    #     for product in products:
    #         product.versions = Version.objects.filter(product=product)
    #         product.version = product.versions.filter(is_current=True).first()
    #
    #     return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        category_data = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_data.pk
        context_data['title'] = f'{category_data.name}'
        for product in context_data.get('object_list'):
            product.version = product.version_set.filter(is_current=True).first()
        return context_data


class ProductDetailView(DetailView):
    """Класс для вывода информации о продукте по его pk"""
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        versions = Version.objects.filter(product=product)
        context['versions'] = versions
        current_version = versions.filter(is_current=True).first()
        context['current_version'] = current_version

        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:category_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:category_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:category_list')
