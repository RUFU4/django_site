from django.contrib import admin
from products.models import Product
from users.models import User

admin.site.register(Product)
admin.site.register(User)