# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import UserSerializer, AlunoSerializer
from .models import User, Aluno

class UserViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = User.objects.all()

	# specify serializer to be used
	serializer_class = UserSerializer

class AlunoViewSet(viewsets.ModelViewSet):
	queryset = Aluno.objects.all()

	serializer_class = AlunoSerializer