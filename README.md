# BackEnd project EduPlay

### Após realizar o clone do projeto siga os passos abaixo para a instalação das dependencias

## Inicie a aplicação criando o projeto Venv

```
py -m venv venv
./venv/Scripts/activate
```

## Instalando os demais requerimentos do projeto

```
pip install -r requirements.txt
```

## Django REST framework
https://www.django-rest-framework.org/#development

```
pip install django
pip install djangorestframework
pip install django-cors-headers
```

## Sempre que tiver uma class de uma tabela nova no arquivo de models deve usar os seguintes comandos a seguir

```
py manage.py makemigrations
py manage.py migrate
```

## informações sobre chave estrangeira encontradas Django

```
https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#referencing-the-user-model
```

## Inicie o projeto

```
py manage.py runserver
```

## Urls para requisições
### Teste
```
"usuarios": "http://127.0.0.1:8000/usuarios/",
"alunos": "http://127.0.0.1:8000/alunos/"
```

### Produção
```
```
