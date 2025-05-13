from rest_framework import serializers
from .models import Aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['re_alu', 'nome_alu', 'data_nascimento_alu', 'cpf_alu', 'nome_responsavel_alu', 'documento_alu']
