
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracoesViewSet
from localizacao.api.viewsets import LocalizacaoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet)
router.register(r'atracoes', AtracoesViewSet)
router.register(r'localizacao', LocalizacaoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'avaliacao', AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
