from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Aluno
from .serializers import AlunoSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


# ViewSet para API REST do modelo Aluno
class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('password')

        user = authenticate(request, username=username, password=senha)
        if user is not None:
            login(request, user)
            return redirect('home')  # nome da URL da home_view
        else:
            return render(request, 'telegrama/login.html', {'erro': 'Usuário ou senha inválidos.'})

    return render(request, 'telegrama/login.html')


@login_required
def home_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        re = request.POST.get('re', '').strip()
        senha = request.POST.get('senha', '').strip()

        if not nome or not re or not senha:
            return render(request, 'telegrama/home.html', {'erro': 'Todos os campos são obrigatórios.'})

        try:
            aluno = Aluno.objects.get(re_alu=re)
        except Aluno.DoesNotExist:
            # Aqui manda a mensagem correta sem quebrar
            return render(request, 'telegrama/home.html', {'erro': 'Aluno não encontrado.'})

        if aluno.nome_alu.lower() != nome.lower():
            return render(request, 'telegrama/home.html', {'erro': 'Aluno não encontrado.'})

        cpf_limpo = ''.join(filter(str.isdigit, aluno.cpf_alu or ''))
        if senha == cpf_limpo[:4]:
            request.session['aluno_id'] = aluno.re_alu
            return redirect('pesquisa')
        else:
            return render(request, 'telegrama/home.html', {'erro': 'Senha incorreta.'})

    return render(request, 'telegrama/home.html')




@login_required
def pesquisa_view(request):
    aluno_id = request.session.get('aluno_id')
    if not aluno_id:
        return redirect('home')

    try:
        aluno = Aluno.objects.get(re_alu=aluno_id)
    except Aluno.DoesNotExist:
        return redirect('home')

    documento_status = aluno.documento_alu.strip().lower() if aluno.documento_alu else ''
    if documento_status == 'ok':
        mensagem = "Documentos: OK"
    else:
        mensagem = "Documentos: pendentes"

    return render(request, 'telegrama/pesquisa.html', {
        'aluno': aluno,
        'documentos_status': mensagem,
    })
