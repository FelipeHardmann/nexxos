import requests

api = 'https://api.nasa.gov/planetary/apod?api_key=A3J5b6roKJRB5SYJczjbgwJQcnT6DYVY49czQZiV'
request = requests.get(api)

dados = request.json()
date = dados['date']
explicacao = dados['explanation']
url = dados['url']
title = dados['title']

img = requests.get(url)

with open(f'{title}.jpg', 'wb') as file:
    file.write(img.content)

print(f'O título da imagem é: {title}\nA data que foi tirada foi em {date}\nA sua explicação: {explicacao}')
