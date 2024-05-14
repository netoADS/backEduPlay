# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import User, Aluno, Tema, Questionario, Nota

# Create a model serializer


class UserSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = User
        fields = '__all__'


class AlunoSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Aluno
        fields = '__all__'


class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tema
        fields = '__all__'


class QuestionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionario
        fields = '__all__'


class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = '__all__'
