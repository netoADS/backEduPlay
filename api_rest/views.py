# import viewsets
from rest_framework import viewsets

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# import local data
from .serializers import UserSerializer, AlunoSerializer
from .models import User, Aluno

import json


class UserViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = User.objects.all()

    # specify serializer to be used
    serializer_class = UserSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()

    serializer_class = AlunoSerializer


