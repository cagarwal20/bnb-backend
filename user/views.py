from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User,Cart
from .serializers import UserSerializer,CartSerializer
# Create your views here.


class Info(APIView):
    def get(self,request):
        obj = User.objects.all()
        ser_data = UserSerializer(obj,many=True)
        return Response({"data":ser_data.data} , status=200)

class Cart_View(APIView):
    def get(self,request):
        obj = Cart.objects.all()
        ser_data = CartSerializer(obj,many=True)
        return Response({"data":ser_data.data} , status=200)



class ping(APIView):
    def get(self,request):
        return Response({"response":"i am alive"} , status=400)