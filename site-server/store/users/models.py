from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    shipping_address = models.CharField(max_length=500)
    postal_code = models.CharField(max_length=20)
    


