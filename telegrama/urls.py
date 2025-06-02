from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AlunoViewSet,
    LoginAPIView, VerificaAlunoAPIView, PesquisaAPIView
)

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)

urlpatterns = [
    # Rotas REST para o modelo Aluno (CRUD)
    path('api/', include(router.urls)),

    # Rotas para páginas HTML com Django REST Framework + TemplateHTMLRenderer
    path('login/', LoginAPIView.as_view(), name='login'),
    path('home/', VerificaAlunoAPIView.as_view(), name='home'),
    path('pesquisa/', PesquisaAPIView.as_view(), name='pesquisa'),
]
