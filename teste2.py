import requests

user = int(input('Digite o usuario que você está procurando: '))

api = f'https://jsonplaceholder.typicode.com/todos/{user}'
request = requests.get(api)
dados = request.json()

id_user = dados['id']
title = dados['title']
completed = dados['completed']

if completed:
    valor = 'Completo'
else:
    valor = 'Incompleto'

print(f'O usuário {user}, possui o ID: {id_user}, o titulo {title} e ele está {valor}')
