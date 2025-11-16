from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import ProdutosViewSet, RegisterView, MeView, CartViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register('produtos', ProdutosViewSet, basename='Produtos')
router.register('carrinho', CartViewSet, basename='Carrinho')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/me/', MeView.as_view(), name='me'),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
