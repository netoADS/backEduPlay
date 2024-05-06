from django.urls import path
from api_rest.views import UserViewSet, AlunoViewSet

urlpatterns = [
    path('usuarios/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='usuarios-list'),
    path('usuarios/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='usuarios-detail'),
    path('alunos/', AlunoViewSet.as_view({'get': 'list', 'post': 'create'}), name='alunos-list'),
    path('alunos/<int:pk>/', AlunoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='alunos-detail'),
]
