from django.db import models

class Aluno(models.Model):
    re_alu = models.CharField(max_length=20, primary_key=True)
    nome_alu = models.CharField(max_length=255)
    data_nascimento_alu = models.DateField()
    cpf_alu = models.CharField(max_length=14, blank=True, null=True)
    nome_responsavel_alu = models.CharField(max_length=255)
    documento_alu = models.CharField(max_length=255)

    class Meta:
        db_table = 'Alunos'
        managed = False  # Indica que o Django não deve gerenciar a tabela

    def __str__(self):
        return self.nome_alu
