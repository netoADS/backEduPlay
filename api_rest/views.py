from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, AlunoSerializer
from .models import User, Aluno

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
        serializer = AlunoSerializer(data=request.data)
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
