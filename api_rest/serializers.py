# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import User, Aluno

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
