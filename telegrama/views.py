from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework import status
from .models import Aluno
from .serializers import AlunoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

# Login API + template
class LoginAPIView(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = 'telegrama/login.html'

    def get(self, request):
        return Response()

    def post(self, request):
        username = request.data.get('username', '').strip()
        password = request.data.get('password', '').strip()

        if username == 'admin' and password == 'univesp-pi3':
            request.session['admin_logged_in'] = True
            return redirect('home')

        return Response({'erro': 'Usuário ou senha incorretos.'}, status=status.HTTP_401_UNAUTHORIZED)

# Verifica (Home) API + template
class VerificaAlunoAPIView(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = 'telegrama/home.html'

    def get(self, request):
        return Response()

    def post(self, request):
        nome = request.data.get('nome', '').strip()
        re = request.data.get('re', '').strip()
        senha = request.data.get('senha', '').strip()

        if not nome or not re or not senha:
            return Response({'erro': 'Todos os campos são obrigatórios.'}, template_name=self.template_name, status=status.HTTP_400_BAD_REQUEST)

        try:
            aluno = Aluno.objects.get(re_alu=re)
        except Aluno.DoesNotExist:
            return Response({'erro': 'Aluno não encontrado.'}, template_name=self.template_name, status=status.HTTP_404_NOT_FOUND)

        if aluno.nome_alu.lower() != nome.lower():
            return Response({'erro': 'Aluno não encontrado.'}, template_name=self.template_name, status=status.HTTP_404_NOT_FOUND)

        cpf_limpo = ''.join(filter(str.isdigit, aluno.cpf_alu or ''))
        if senha == cpf_limpo[:4]:
            request.session['aluno_id'] = aluno.re_alu

            # Calcula status do documento aqui também
            doc = (aluno.documento_alu or "").strip().lower()
            if doc == "ok":
                documentos_status = "Sem pendências"
            else:
                documentos_status = "Cadastro incompleto"

            return Response({'aluno': aluno, 'documentos_status': documentos_status}, template_name='telegrama/pesquisa.html')
        else:
            return Response({'erro': 'Senha incorreta.'}, template_name=self.template_name, status=status.HTTP_401_UNAUTHORIZED)

# Pesquisa API + template
class PesquisaAPIView(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = 'telegrama/pesquisa.html'

    def get(self, request):
        aluno_id = request.session.get('aluno_id')
        if not aluno_id:
            return redirect('home')

        try:
            aluno = Aluno.objects.get(re_alu=aluno_id)
        except Aluno.DoesNotExist:
            return redirect('home')

        doc = (aluno.documento_alu or "").strip().lower()
        if doc == "ok":
            documentos_status = "Sem pendências"
        else:
            documentos_status = "Cadastro incompleto"

        return Response({'aluno': aluno, 'documentos_status': documentos_status})
