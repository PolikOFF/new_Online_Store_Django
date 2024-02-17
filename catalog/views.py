from django.shortcuts import render, get_object_or_404
from catalog.models import Category, Product


def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'SkyStore - Главная'
    }
    return render(request, 'catalog/categories.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} {phone} {message}')
    return render(request, 'catalog/contacts.html')


def category(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Все категории продуктов'
    }
    return render(request, 'catalog/category.html', context)


def product_info(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Все продукты категории "{category_item}"'
    }
    return render(request, 'catalog/product_info.html', context)


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'object': product
    }
    return render(request, 'catalog/product_details.html', context)
