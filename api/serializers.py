from rest_framework import serializers
from api.models import Products

class ProductsSerializers(serializers.ModelSerializer):
    imagem_url = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = [
            'id', 'titulo', 'descricao', 'preco', 'categoria',
            'marca', 'modelo', 'codpro', 'imagem_url', 'pid', 'cor'
        ]

    def get_imagem_url(self, obj):
        request = self.context.get('request')
        if obj.imagens and hasattr(obj.imagens, 'url'):
            return request.build_absolute_uri(obj.imagens.url)
        return None
    