from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import login_view, home_view, pesquisa_view, AlunoViewSet

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)

urlpatterns = [
    path('', include(router.urls)),  # API REST
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),         # login
    path('pesquisa/', pesquisa_view, name='pesquisa'),  # página com dados do aluno
]
