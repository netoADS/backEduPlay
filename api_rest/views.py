# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import UserSerializer
from .models import User

# create a viewset


class UserViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = User.objects.all()

	# specify serializer to be used
	serializer_class = UserSerializer
