# Generated by Django 4.2.21 on 2025-05-21 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('re_alu', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nome_alu', models.CharField(max_length=100)),
                ('data_nascimento_alu', models.DateField()),
                ('cpf_alu', models.CharField(max_length=14)),
                ('nome_responsavel_alu', models.CharField(max_length=100)),
                ('documento_alu', models.CharField(max_length=50)),
            ],
        ),
    ]
