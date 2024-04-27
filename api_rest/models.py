from django.db import models

from api_root import settings

# Create your models here.
class User(models.Model):
    user_firebase_id = models.CharField(max_length=255, default='')
    user_email = models.EmailField(default='')
    user_level = models.IntegerField(default=0)
    user_dataCadastro = models.DateTimeField(default='')

    def __str__(self):
        return f'Email: {self.user_email} | Firebase: {self.user_firebase_id}'

class Pessoa(models.Model):
    pessoa_nickname = models.CharField(max_length=100, default='')
    pessoa_nome = models.CharField(max_length=150, default='')

    def __str__(self):
        return f'UserName: {self.pessoa_nickname} | Nome: {self.pessoa_nome}'


class User_Pessoa(models.Model):
    pessoa = models.ForeignKey(Pessoa, null=True, name='FK_PESSOA', related_name='FK_PESSOA', on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, name='FK_USER', related_name='FK_USER', on_delete=models.SET_NULL)
    


class Aluno(models.Model):
    aluno_email = models.EmailField(default='')
    aluno_pass = models.CharField(max_length=255, default='')
    aluno_idade = models.IntegerField(default=0)
    aluno_dataCadastro = models.DateTimeField(default='')

    def __str__(self):
        return f'Email: {self.aluno_email} | Senha: {self.aluno_pass}'
    

class Aluno_Pessoa(models.Model):
    pessoa = models.ForeignKey(Pessoa, null=True, name='FK_PESSOA_ALUNO', related_name='FK_PESSOA_ALUNO', on_delete=models.SET_NULL)
    aluno = models.ForeignKey(Aluno, null=True, name='FK_ALUNO', related_name='FK_ALUNO', on_delete=models.SET_NULL)
    

#class tema(models.Model):
#    tema = models.CharField(max_length=150, default='')
#    classification = models.CharField(max_length=1, default='')


#class tema_questionario(models.Model):


#class QuestionarioQuestion(models.Model):
#    question1 = models.CharField(max_length=1000, default='')
#    question2 = models.CharField(max_length=1000, default='')
#    question3 = models.CharField(max_length=1000, default='')
#    question4 = models.CharField(max_length=1000, default='')
#    question5 = models.CharField(max_length=1000, default='')
#    dataInicio = models.DateTimeField(default='')


#class QuestionarioResp(models.Model):
#    resp_quest1 = models.CharField(max_length=1000, default='')
#    resp_quest2 = models.CharField(max_length=1000, default='')
#    resp_quest3 = models.CharField(max_length=1000, default='')
#    resp_quest4 = models.CharField(max_length=1000, default='')
#    resp_quest5 = models.CharField(max_length=1000, default='')
#    dataentrega = models.DateTimeField(default='')




# base para teste de urls
#class GeeksModel(models.Model):
#    title = models.CharField(max_length=200)
#    description = models.TextField()
# 
#    def __str__(self):
#        return self.title
