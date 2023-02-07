from rest_framework import serializers
from .models import Product,Reviews
class ProductSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["price",
            "product_type",
            "image_url",
            "size",
            "flavour",
            "mrp",
            "discount",
            "price",
            "details"]
    def get_price(self,obj):
        return obj.mrp*(1 - obj.discount/100)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

    
    
