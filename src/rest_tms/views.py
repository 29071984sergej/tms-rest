from itertools import product

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from rest_tms.models import Product
from rest_tms.serializer import ProductSerializer


# from rest_tms.models import Product
# from rest_tms.serializer import ProductSerializer
#
#
# @api_view(['GET', 'POST'])
# def products(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         return Response(serializer.data)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def get_products_deteil(request, pk):
#     product = Product.objects.get(pk=pk)
#     if request.method == 'GET':
#         serializer = ProductSerializer(products)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ProductSerializer(products, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=200)
#         return Response(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         products.delete()
#         return Response(status=204)
#
#
# class Products(APIView)
#     def products(request):
#         if request.method == 'GET':
#             products = Product.objects.all()
#             serializer = ProductSerializer(products, many=True)
#             return Response(serializer.data)
#         elif request.method == 'POST':
#             serializer = ProductSerializer(data=request.data)
#             return Response(serializer.data)
#
#
# class ProductDetail(APIView)
#     def get(self,request, pk):
#         product = Product.objects.get(pk=pk)
#         if request.method == 'GET':
#             serializer = ProductSerializer(products)
#             return Response(serializer.data)
#
#     def put(self, request, pk):
#         serializer = ProductSerializer(products, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=200)
#         return Response(serializer.errors, status=400)
#     def delete(self, request, pk):
#         product = Product.objects.get(pk=pk)
#         products.delete()
#         return Response(status=204)

# class Products(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def get_queryset(self):
#         queryset = super(Products, self).get_queryset()
#         queryset = queryset.filter(visible=True)
#         return queryset
#
#
# class ProductDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


class ProductDetail(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
