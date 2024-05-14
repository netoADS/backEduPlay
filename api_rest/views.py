from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, AlunoSerializer, TemaSerializer, QuestionarioSerializer, NotaSerializer
from .models import User, Aluno, Tema, Questionario, Nota


class UserViewSet(viewsets.ViewSet):
    # Listagem de usuários
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    # Recuperação de um usuário específico
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # Criação de um novo usuário
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Atualização de um usuário existente
    def update(self, request, pk=None):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Exclusão de um usuário
    def destroy(self, request, pk=None):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlunoViewSet(viewsets.ViewSet):
    # Listagem de alunos
    def list(self, request):
        queryset = Aluno.objects.all()
        serializer = AlunoSerializer(queryset, many=True)
        return Response(serializer.data)

    # Recuperação de um aluno específico
    def retrieve(self, request, pk=None):
        queryset = Aluno.objects.all()
        aluno = get_object_or_404(queryset, pk=pk)
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data)

    # Criação de um novo aluno
    def create(self, request):
        data = request.data
        print(data)
        professor_id = data.get('professor')  # Obter o ID do professor dos dados da requisição
        if not professor_id:
            return Response({"detail": "O ID do professor é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        # Adicionar o professor ao dicionário de dados
        data['professor'] = professor_id
        print(data)
        serializer = AlunoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Atualização de um aluno existente
    def update(self, request, pk=None):
        aluno = Aluno.objects.get(pk=pk)
        serializer = AlunoSerializer(aluno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Exclusão de um aluno
    def destroy(self, request, pk=None):
        aluno = Aluno.objects.get(pk=pk)
        aluno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TemaViewSet(viewsets.ViewSet):
    # Listagem de temas
    def list(self, request):
        queryset = Tema.objects.all()
        serializer = TemaSerializer(queryset, many=True)
        return Response(serializer.data)

    # Recuperação de um tema específico
    def retrieve(self, request, pk=None):
        queryset = Tema.objects.all()
        tema = get_object_or_404(queryset, pk=pk)
        serializer = TemaSerializer(tema)
        return Response(serializer.data)

    # Criação de um novo tema
    def create(self, request):
        serializer = TemaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Atualização de um tema existente
    def update(self, request, pk=None):
        tema = Tema.objects.get(pk=pk)
        serializer = TemaSerializer(tema, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Exclusão de um tema
    def destroy(self, request, pk=None):
        tema = Tema.objects.get(pk=pk)
        tema.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuestionarioViewSet(viewsets.ViewSet):
    # Listagem de questionarios
    def list(self, request):
        queryset = Questionario.objects.all()
        serializer = QuestionarioSerializer(queryset, many=True)
        return Response(serializer.data)

    # Recuperação de um questionario específico
    def retrieve(self, request, pk=None):
        queryset = Questionario.objects.all()
        questionario = get_object_or_404(queryset, pk=pk)
        serializer = QuestionarioSerializer(questionario)
        return Response(serializer.data)

    # Criação de um novo questionario
    def create(self, request):
        serializer = QuestionarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Atualização de um questionario existente
    def update(self, request, pk=None):
        questionario = Questionario.objects.get(pk=pk)
        serializer = QuestionarioSerializer(questionario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Exclusão de um questionario
    def destroy(self, request, pk=None):
        questionario = Questionario.objects.get(pk=pk)
        questionario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NotaViewSet(viewsets.ViewSet):
    # Listagem de notas
    def list(self, request):
        queryset = Nota.objects.all()
        serializer = NotaSerializer(queryset, many=True)
        return Response(serializer.data)

    # Recuperação de uma nota específica
    def retrieve(self, request, pk=None):
        queryset = Nota.objects.all()
        nota = get_object_or_404(queryset, pk=pk)
        serializer = NotaSerializer(nota)
        return Response(serializer.data)

    # Criação de uma nova nota
    def create(self, request):
        serializer = NotaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Atualização de uma nota existente
    def update(self, request, pk=None):
        nota = Nota.objects.get(pk=pk)
        serializer = NotaSerializer(nota, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Exclusão de uma nota
    def destroy(self, request, pk=None):
        nota = Nota.objects.get(pk=pk)
        nota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
