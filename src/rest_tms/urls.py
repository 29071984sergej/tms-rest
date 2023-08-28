from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_tms.views import ProductDetail, Product

#from rest_tms.views import products, get_product_detail

#
routers = routers.DefaultRouter()
routers.register('products', ProductDetail)
print(routers.urls)

urlpatterns = [
    #path('', Products.as_view({'get':'list', 'post': 'create'})),
    # path('<int:pk>/', ProductDetail.as_view({})),
    path('', include(routers.urls))
]