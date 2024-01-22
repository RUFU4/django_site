from django.db import models
from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to='products_images')
    category = models.CharField(max_length=200)

    def __str__(self):
        return f'Товар: {self.name} | Цена: {self.price}'
    
class Basket(models.Model):
    users = models.ForeignKey(to = User, on_delete=models.CASCADE)
    product = models.ForeignKey(to = Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'Корзина для {self.user.email} | Продукт: {self.product.name}'