from django.db import models

class Aluno(models.Model):
    re_alu = models.CharField(max_length=20, primary_key=True)
    nome_alu = models.CharField(max_length=100)
    data_nascimento_alu = models.DateField()
    cpf_alu = models.CharField(max_length=14)  # CPF pode ter máscara
    nome_responsavel_alu = models.CharField(max_length=100)
    documento_alu = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_alu

    class Meta:
        db_table = 'alunos'
