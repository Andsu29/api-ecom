from django.shortcuts import render
from rest_framework import viewsets
from api.models import Products
from api.serializers import ProductsSerializers

class ProdutosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers

    def get_serializer_context(self):
        return {'request': self.request}