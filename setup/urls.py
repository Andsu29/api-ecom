from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import ProdutosViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('produtos', ProdutosViewSet, basename='Produtos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
