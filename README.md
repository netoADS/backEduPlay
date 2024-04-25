# BackEnd project EduPlay

## Criando venv do projeto

```
py -m venv venv
./venv/Scripts/activate
```

## Django REST framework
https://www.django-rest-framework.org/#development

```
pip install django
pip install djangorestframework
pip install django-cors-headers
```

Sempre que tiver uma class de uma tabela nova no arquivo de models deve usar os seguintes comandos a seguir

```
py manage.py makemigrations
py manage.py migrate
```
