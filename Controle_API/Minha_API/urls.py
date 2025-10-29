from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicamentoViewSet, ClienteViewSet, VendaViewSet, EstoqueViewSet

# Roteador automático do DRF
router = DefaultRouter()
router.register(r'medicamentos', MedicamentoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'vendas', VendaViewSet)
router.register(r'estoque', EstoqueViewSet)

urlpatterns = router.urls
    
