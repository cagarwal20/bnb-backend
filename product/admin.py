from django.contrib import admin
from product.models import Product,Authenticity,Reviews
# Register your models here.
admin.site.register(Product)
admin.site.register(Authenticity)
admin.site.register(Reviews)