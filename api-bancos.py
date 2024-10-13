# Alpha Vantage

# Pegando cotações semanais JSON

chave_api = "PIIXESQLS85040Z6"

import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=GOOG&apikey={chave_api}'
r = requests.get(url)
data = r.json()

display(data)

# Pegando cotações semanais CSV

import pandas as pd
from io import StringIO

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=IBM&apikey={chave_api}&datatype=csv'
r = requests.get(url)

tabela = pd.read_csv(StringIO(r.text))
display(tabela)

# Cotações

acoes = ['ITUB4', 'ABEV3', 'BBAS3']

compilada = pd.DataFrame()

for acao in acoes:
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={acao}.SAO&apikey={chave_api}&datatype=csv'
    r = requests.get(url)
    tabela = pd.read_csv(StringIO(r.text))
    lista_tabelas = [compilada, tabela]
    compilada = pd.concat(lista_tabelas)
    
display(compilada)

# Encontrar ativos

url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=amazon&apikey={chave_api}&datatype=csv'
r = requests.get(url)

tabela = pd.read_csv(StringIO(r.text))
display(tabela)

# Informações de resultado

url = f'https://www.alphavantage.co/query?function=EARNINGS&symbol=AMZN&apikey={chave_api}'
r = requests.get(url)
data = r.json()

print(data)