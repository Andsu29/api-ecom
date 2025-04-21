from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import ProdutosViewSet

router = routers.DefaultRouter()
router.register('produtos', ProdutosViewSet, basename='Produtos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
