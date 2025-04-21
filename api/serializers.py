from rest_framework import serializers
from api.models import Products
import base64

class ProductsSerializers(serializers.ModelSerializer):
    imagens = serializers.SerializerMethodField()
    class Meta:
        model = Products
        fields = ['id', 'titulo', 'descricao', 'preco', 'categoria', 'marca', 'modelo', 'codpro', 'imagens', 'pid', 'cor']

    def get_imagens(self, obj):
        # Converte os dados binários da imagem para base64
        if obj.imagens:
            return base64.b64encode(obj.imagens).decode('utf-8')
        return None