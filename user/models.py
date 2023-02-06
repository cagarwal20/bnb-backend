from django.db import models
import uuid
from product.models import Product
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart_details = models.ManyToManyField(Product)