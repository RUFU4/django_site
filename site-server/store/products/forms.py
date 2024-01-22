from products.models import Product
from django.forms import ModelForm, TextInput, FileInput, ImageField


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','image','category']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'class': 'image-brand-ph',
                'placeholder': 'Название Товара'
            }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'class': 'price-item-ph',
                'placeholder': 'Укажите цену в руб.'
            }),
            "image":FileInput(attrs={
                'class': 'form-control',
                'class': 'image-ph',
                'placeholder': 'Изображение'
            }),
                  
            "category": TextInput(attrs={
                'class': 'form-control',
                'class': 'category-ph',
                'placeholder': 'Название Бренда'
            }),     
        }