# basic URL Configurations
from django.urls import include, path
# import routers
from rest_framework import routers

# import everything from views
from api_rest.views import *

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'usuarios', UserViewSet, basename='Usuarios')
router.register(r'alunos', AlunoViewSet, basename='Alunos')

# specify URL Path for rest_framework
urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls'))
]

