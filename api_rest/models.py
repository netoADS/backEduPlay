from django.db import models

from api_root import settings


class Pessoa(models.Model):
    pessoa_nickname = models.CharField(max_length=100, default='')
    pessoa_nome = models.CharField(max_length=150, default='')

    class Meta:
        abstract = True

    def __str__(self):
        return f'UserName: {self.pessoa_nickname} | Nome: {self.pessoa_nome}'


class User(Pessoa):
    # pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE, parent_link=True, related_name='pessoas', null=False, blank=False, )
    user_firebase_id = models.CharField(max_length=255, default='')
    user_email = models.EmailField(default='')
    user_level = models.IntegerField(default=0)
    user_dataCadastro = models.DateTimeField(default='')

    def __str__(self):
        return f'Email: {self.user_email} | Firebase: {self.user_firebase_id}'


class Aluno(Pessoa):
    aluno_id_login = models.IntegerField(default=0)
    aluno_pass = models.CharField(max_length=255, default='')
    aluno_idade = models.IntegerField(default=0)
    aluno_dataCadastro = models.DateTimeField(default='')
    professor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='alunos', default=0)

    def __str__(self):
        return f'Email: {self.aluno_email} | Senha: {self.aluno_pass}'


class Tema(models.Model):
    tema = models.CharField(max_length=150, default='')
    classification = models.CharField(max_length=1, default='')
    professor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='temas')


class Questionario(models.Model):
    pergunta = models.CharField(max_length=1000, default='')
    resposta1 = models.CharField(max_length=1000, default='')
    resposta2 = models.CharField(max_length=1000, default='')
    resposta3 = models.CharField(max_length=1000, default='')
    resposta4 = models.CharField(max_length=1000, default='')
    dataInicio = models.DateTimeField(default='')
    dataFinal = models.DateTimeField(default='')
    tema = models.ForeignKey(
        Tema, on_delete=models.CASCADE, related_name='questionarios', null=True, blank=True)
    professor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='questionarios')


class Nota(models.Model):
    aluno = models.ForeignKey(
        Aluno, on_delete=models.CASCADE, related_name='respostas')
    questionario = models.ForeignKey(
        Questionario, on_delete=models.CASCADE, related_name='respostas')
    resposta = models.CharField(max_length=1000, default='')
    nota = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'Aluno: {self.aluno}, Questionário: {self.questionario}, Resposta: {self.resposta}'


# class User_Pessoa(models.Model):
#    pessoa = models.ForeignKey(Pessoa, null=True, name='FK_PESSOA', related_name='FK_PESSOA', on_delete=models.SET_NULL)
#    user = models.ForeignKey(User, null=True, name='FK_USER', related_name='FK_USER', on_delete=models.SET_NULL)
