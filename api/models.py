from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(max_length=255, null=True, blank=True)
    preco = models.IntegerField(null=True, blank=True)
    categoria = models.CharField(max_length=255, null=True, blank=True)
    marca = models.CharField(max_length=255, null=True, blank=True)
    modelo = models.CharField(max_length=255, null=True, blank=True)
    codpro = models.CharField(max_length=255, null=True, blank=True)
    imagens = models.ImageField(upload_to='produtos/', null=True, blank=True)
    pid = models.IntegerField(null=True, blank=True)
    cor = models.CharField(max_length=255, null=True, blank=True)
    qtd_estoque = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'produtos' 

    def __str__(self):
        return self.titulo

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")

    class Meta:
        db_table = 'carrinho' 

    def __str__(self):
        return f"Carrinho de {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    produto = models.ForeignKey(Products, on_delete=models.CASCADE)
    qtd = models.IntegerField(default=1)

    class Meta:
        db_table = 'itens_carrinho' 

    @property
    def titulo(self):
        return self.produto.titulo

    @property
    def preco(self):
        return self.produto.preco

    def subtotal(self):
        return self.preco * self.qtd