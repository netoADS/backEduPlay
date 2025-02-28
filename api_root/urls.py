from django.urls import path
from api_rest.views import UserViewSet, AlunoViewSet, TemaViewSet, QuestionarioViewSet, NotaViewSet

urlpatterns = [

    # URLs para usuarios
    path('usuarios/',
         UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='usuarios-list'),
    path('usuarios/<int:pk>/', UserViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='usuarios-detail'),

    # URLs para Alunos
    path('alunos/',
         AlunoViewSet.as_view({'get': 'list', 'post': 'create'}), name='alunos-list'),
    path('alunos/<int:pk>/', AlunoViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='alunos-detail'),

    # URL para listagem de alunos de um professor específico
    path('alunos/professor/<int:pk>/', AlunoViewSet.as_view(
        {'get': 'list_by_professor'}), name='alunos-list-by-professor'),

    # URLs para Temas
    path('temas/',
         TemaViewSet.as_view({'get': 'list', 'post': 'create'}), name='temas-list'),
    path('temas/<int:pk>/', TemaViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='temas-detail'),

    # URLs para questionarios
    path('questionarios/', QuestionarioViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='questionarios-list'),
    path('questionarios/<int:pk>/', QuestionarioViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='questionarios-detail'),

    # URL para listagem de questionários de alunos de um professor específico
    path('questionarios/professor/<int:pk>/', QuestionarioViewSet.as_view(
        {'get': 'list_by_professor'}), name='questionarios-list-by-professor'),

    # URLs para notas
    path('notas/',
         NotaViewSet.as_view({'get': 'list', 'post': 'create'}), name='notas-list'),
    path('notas/<int:pk>/', NotaViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='notas-detail'),
]
