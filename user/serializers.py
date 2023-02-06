from rest_framework import serializers
from .models import User,Cart
class UserSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField()
    # content = serializers.CharField(max_length=200)
    # created = serializers.DateTimeField()
    class Meta:
        model = User
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField()
    # content = serializers.CharField(max_length=200)
    # created = serializers.DateTimeField()
    class Meta:
        model = Cart
        fields = "__all__"