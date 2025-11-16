from django.shortcuts import render
from rest_framework import viewsets
from api.models import Products, Cart
from api.serializers import ProductsSerializers, CartSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated

class ProdutosViewSet(viewsets.ReadOnlyModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers

    def get_serializer_context(self):
        return {'request': self.request}

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Usuário criado com sucesso!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # só retorna o carrinho do usuário logado
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # força o carrinho a ser do usuário logado
        serializer.save(user=self.request.user)