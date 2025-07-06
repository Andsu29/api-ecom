from django.db import models

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

    class Meta:
        db_table = 'produtos' 

    def __str__(self):
        return self.titulo