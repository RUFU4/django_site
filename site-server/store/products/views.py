from django.shortcuts import render, redirect, HttpResponseRedirect
from products.models import Product
from products.forms import ProductForm
from products.models import Basket
from users.models import User
from django.urls import reverse

def index(request):
    return render(request, 'products/index.html')


def aboutus(request):
    return render(request, 'products/about-us.html')


def catalog(request):
    context = {
        'title': 'CATALOG',
        'products': Product.objects.all(),
    }

    return render(request, 'products/catalog.html', context)

def add(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog')
        else:
            error = 'Ошибка, друг'

    form = ProductForm

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'products/add.html', data)

def contact(request):
    return render(request, 'products/contact.html')


def faq(request):
    return render(request, 'products/faq.html')

def basket(request):
    context = {basket: Basket.objects.all}
    return render(request, 'products/basket.html', context)

def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user = request.user, product = product)
    if not basket.exists():
        Basket.objects.create(user = request.user, product = product)
    return HttpResponseRedirect(reverse('index'))