from django.urls import path
from catalog.views import category, products, product

urlpatterns = [
    path('category/', category),
    path('', products),
    path('products/<pk>/', product)
]