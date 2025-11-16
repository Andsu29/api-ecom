from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Products, CartItem, Cart

class ProductsSerializers(serializers.ModelSerializer):
    imagem_url = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = [
            'id', 'titulo', 'descricao', 'preco', 'categoria',
            'marca', 'modelo', 'codpro', 'imagem_url', 'pid', 'cor', 'qtd_estoque'
        ]

    def get_imagem_url(self, obj):
        request = self.context.get('request')
        if obj.imagens and hasattr(obj.imagens, 'url'):
            return request.build_absolute_uri(obj.imagens.url)
        return None

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["id", "produto", "titulo", "preco", "qtd"]

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ["id", "user", "items"]

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        cart = Cart.objects.create(**validated_data)

        for item_data in items_data:
            CartItem.objects.create(cart=cart, **item_data)

        return cart

    def update(self, instance, validated_data):
        items_data = validated_data.pop("items")
        
        # Atualiza dados básicos do carrinho (se tiver)
        instance.user = validated_data.get("user", instance.user)
        instance.save()

        # Limpa os itens antigos
        instance.items.all().delete()

        # Recria os itens com os novos dados
        for item_data in items_data:
            CartItem.objects.create(cart=instance, **item_data)

        return instance