# Pegando cotação de 1 ação

from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt

cotacao_bovespa = web.DataReader('^BVSP', data_source='yahoo', start="01/01/2024", end="01/01/2025")
display(cotacao_bovespa)
cotacao_bovespa["Adj Close"].plot(figsize=(15, 10))
plt.show()

cotacao_petr = web.DataReader('PETR4.SA', data_source='yahoo', start="01/01/2024", end="01/01/2025")
display(cotacao_petr)
cotacao_petr["Adj Close"].plot(figsize=(15, 10))
plt.show()

# Pegando cotação de uma carteira de ações em um intervalo de datas específico

from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt

tabela_empresas = pd.read_excel(r"P:/Guilherme/Python/Empresas.xlsx")
display(tabela_empresas)

for empresa in tabela_empresas['Empresas']:
        print(empresa)
        cotacao = web.DataReader(f'{empresa}.SA', data_source='yahoo', start="01/01/2024", end="01/01/2025")
        display(cotacao)
        cotacao["Adj Close"].plot(figsize=(15, 10))
        plt.show()

