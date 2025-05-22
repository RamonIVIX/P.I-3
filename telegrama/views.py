from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Aluno
from .serializers import AlunoSerializer

# ViewSet para API REST do modelo Aluno
class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

# Página de login do aluno (validação simples)
def home_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        re = request.POST.get('re', '').strip()  # campo "re"
        senha = request.POST.get('senha', '').strip()

        if not nome or not re or not senha:
            return render(request, 'telegrama/home.html', {'erro': 'Todos os campos são obrigatórios.'})

        try:
            aluno = Aluno.objects.get(re_alu=re)
        except Aluno.DoesNotExist:
            return render(request, 'telegrama/home.html', {'erro': 'Dados inválidos.'})

        # Verifica se o nome bate ignorando maiúsculas/minúsculas
        if aluno.nome_alu.lower() != nome.lower():
            return render(request, 'telegrama/home.html', {'erro': 'Dados inválidos.'})

        # Limpa o CPF para ter só números e compara os 4 primeiros dígitos
        cpf_limpo = ''.join(filter(str.isdigit, aluno.cpf_alu or ''))
        if senha == cpf_limpo[:4]:
            request.session['aluno_id'] = aluno.re_alu
            return redirect('pesquisa')
        else:
            return render(request, 'telegrama/home.html', {'erro': 'Senha incorreta.'})

    return render(request, 'telegrama/home.html')

# Página de pesquisa / exibição do status dos documentos
def pesquisa_view(request):
    aluno_id = request.session.get('aluno_id')
    if not aluno_id:
        return redirect('home')

    try:
        aluno = Aluno.objects.get(re_alu=aluno_id)
    except Aluno.DoesNotExist:
        return redirect('home')

    # Avalia status do documento
    documento_status = aluno.documento_alu.strip().lower() if aluno.documento_alu else ''
    if documento_status == 'ok':
        mensagem = "Documentos: OK"
    else:
        mensagem = "Documentos: pendentes"

    return render(request, 'telegrama/pesquisa.html', {
        'aluno': aluno,
        'documentos_status': mensagem,
    })

# Página de login do admin (apenas renderiza o template)
def login_view(request):
    return render(request, 'telegrama/login.html')
