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
"temas": "http://127.0.0.1:8000/temas/"
"questionarios": "http://127.0.0.1:8000/questionarios/"
"notas": "http://127.0.0.1:8000/notas/"
```

### Produção
```
https://backeduplay.onrender.com/usuarios
https://backeduplay.onrender.com/alunos
https://backeduplay.onrender.com/alunos/professor/<idUsuarios>
https://backeduplay.onrender.com/temas
https://backeduplay.onrender.com/questionarios
https://backeduplay.onrender.com/notas
```

## Exemplo de requisição
### GET-ALL
```
TYPE: GET
URL: http://localhost:8000/usuarios/
```

### GET USUARIO EXPECIFICO
```
TYPE: GET
URL: http://localhost:8000/usuarios/<id>/
```

### POST
```
TYPE:POST
URL: http://localhost:8000/usuarios/
BODY:
{
    "pessoa_nickname": "netico",
    "pessoa_nome": "neto gomes",
    "user_firebase_id": "asd1as32d1s32d",
    "user_email": "teste@teste.com",
    "user_level": 3,
    "user_dataCadastro": "2024-04-24T12:32:00Z"
}
```

### PUT
```
TYPE: PUT
URL: http://localhost:8000/usuarios/<id>/
BODY:
{
    "pessoa_nickname": "netico",
    "pessoa_nome": "neto gomes",
    "user_firebase_id": "asd1as32d1s32d",
    "user_email": "teste@teste.com",
    "user_level": 3,
    "user_dataCadastro": "2024-04-24T12:32:00Z"
}
```

### DELETE
```
TYPE: DELETE
URL: http://localhost:8000/usuarios/<id>/
```

```
OBS: É realizado o mesmo padrão para o aluno, porem deve apenas alterar a URL para aluno ao invez de uruasio,
por exemplo: "http://localhost:8000/aluno/" e colocar o tipo de requisição que deseja ser realizada
```

## Formato Json para requisição
### User
```
{
  "pessoa_nickname": "",
  "pessoa_nome": "",
  "user_firebase_id": "",
  "user_email": "",
  "user_level": ,
  "user_dataCadastro": "2024-04-24T12:32:00Z"
},
```

### Aluno
```
{
  "pessoa_nickname": "xaolin matador de porco",
  "pessoa_nome": "neto gomes",
  "aluno_id_login": 12345,
  "aluno_pass": "123456",
  "aluno_idade": 5,
  "aluno_dataCadastro": "2024-04-27T13:34:00Z",
  "professor": <id_Usuario>
}
```

### Tema
```
{
  "tema": "Tema exemplo",
  "classification": "A",
  "professor": <id_Usuario>
}
```
### Questionarios
```
{
  "pergunta": "Qual é a capital da França?",
  "resposta1": "Berlim",
  "resposta2": "Paris",
  "resposta3": "Madrid",
  "resposta4": "Londres",
  "dataInicio": "2024-05-01T00:00:00Z",
  "dataFinal": "2024-05-07T23:59:59Z",
  "tema": <id_tema>,
  "professor": <id_usuario>
}
```
### Notas
```
{
    "resposta": "Rio de Janeiro",
    "nota": null, <nota deve ser atualizada após correção do professor>
    "aluno": <id_aluno>,
    "questionario": <id_questionario>
}
```
