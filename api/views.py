from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import IcecreamSerializer
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from .models import Icecream, Category, Ingredient, Order
class MakeIcecream(APIView):
    serializer_class = IcecreamSerializer

    def post(self, request):
        serializer = IcecreamSerializer(data=request.data)
        if serializer.is_valid():
            icecream = Icecream.objects.create(
                base = serializer.data['base'], 

            )
            categories = Category.objects.all()
            print("!!!!!!!!!!!!!!!!!!!",categories)
            for cat in categories:
            	print("@@@@@@@@@",cat)
            	cat.ingredients.set(serializer.data['categories'])
            	print(">>>>>>>>>>",cat.ingredients.all())

            icecream.save()
            order = Order.objects.create(icecream= icecream)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
