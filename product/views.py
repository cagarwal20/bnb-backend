from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from product.models import Product
from product.serializers import ProductSerializer,ReviewSerializer
from product.models import Authenticity,Reviews
# Create your views here.

class ProductList(APIView):
    def get(self,request):
        data = request.query_params
        if "product_type" in data:
            objects = Product.objects.filter(product_type=data["product_type"])
            obj_data = ProductSerializer(objects , many=True)
            return Response({"data":obj_data.data},status=200)
        objects = Product.objects.all()
        obj_data = ProductSerializer(objects , many=True)
        return Response({"data":obj_data.data},status=200)

class AuthenticityCheck(APIView):
    def get(self,request):
        data = request.query_params
        if "code" in data:
            code = data["code"]
            code = int(code)
            try:
                obj = Authenticity.objects.get(code=code)
            except Authenticity.DoesNotExist:
                obj = None
        if obj is None:
            return Response({"failed" : "fake"} , status=200)
            
        return Response({"success":"authentic"} , status=200)

class AddReview(APIView):
    def post(self,request):
        payload = request.data
        print(payload)
        try:
            obj = Reviews.objects.create(
                name = payload["name"],
                phone_number = payload["phone"],
                email = payload["email"],
                feedback = payload["feedback"]
            )
        except Exception as e:
                obj = None
        if obj:
            return Response({"data" : "success"} , status=200)
        return Response({"data" : "failed"} , status=200)



class Review_List(APIView):
    def get(self,request):
        obj = Reviews.objects.all()
        ser = ReviewSerializer(obj,many=True)
        return Response({"data":
    [
        {
            "id": 25,
            "name": "Moti",
            "email": "123",
            "phone_number": "123",
            "feedback": "wow"
        },
        {
            "id": 26,
            "name": "Lodu",
            "email": "cagarwal20@gmail.com",
            "phone_number": "123",
            "feedback": "wOWWWW"
        },
        {
            "id": 27,
            "name": "Lodu",
            "email": "cagarwal20@gmail.com",
            "phone_number": "123",
            "feedback": "wOWWWW"
        }
    ]
        }
 , status=200)

class ProductVariants(APIView):
    def get(self,request):
        data  = request.query_params
        obj = Product.objects.filter(product_type=data["asset_type"]).values("size").distinct()
        return Response({"data":obj},status=200)