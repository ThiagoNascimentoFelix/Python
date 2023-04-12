import requests
from bs4 import BeautifulSoup


# URL do perfil do Instagram
url = 'https://www.instagram.com/thiagonfelix/'

# Faz uma requisição GET para a página do Instagram
response = requests.get(url)

# Analisa o conteúdo HTML da página usando o BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extrai o título da página
title = soup.title.string

# Imprime o título
print(title)