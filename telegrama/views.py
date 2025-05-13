from rest_framework import viewsets, filters
from .models import Aluno
from .serializers import AlunoSerializer

class AlunoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['re_alu', 'nome_alu']
    