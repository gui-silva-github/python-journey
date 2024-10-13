# Análise de Dados com Python

### Desafio:

## Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.

## O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes. Isso representa uma perda de milhões para a empresa.

## O que a empresa precisa fazer para resolver isso?

## Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing <br>
## Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

import pandas as pd

# Passo 1: Importar as bases de dados da empresa

tabela = pd.read_csv("telecom_users (1).csv")

# Passo 2: Visualizar as bases de dados
# - Entender as informações que a gente tem
# - Descobrir as cagadas da base de dados
# Churn = Cancelamento
# Drop = Largar
# Informação que não te ajuda te atrapalha
# axis=0 -> linha, axis=1 -> coluna
# Edita só essa tabela

tabela = tabela.drop("Unnamed: 0", axis=1)
display(tabela)

# Passo 3: Tratamento de Dados

# valores são reconhecidos da forma errada
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# valores vazios
# colunas completamente vazias
tabela = tabela.dropna(how="all", axis=1)

# linhas com pelo menos 1 valor vazio
tabela = tabela.dropna(how="any", axis=0)

print(tabela.info())

# Passo 4: Análise Inicial (entender como estão os cancelamentos)

print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# Passo 5: Análise Completa (entender o motivo de cancelamento)
# como cada coluna da nossa base de dados impacta no churn

# plotly
# histograma
# para edições nos gráficos: https://plotly.com/python/histograms/

import plotly.express as px

# 2 etapas para criar um gráfico

for coluna in tabela.columns:
    
    # criar o gráfico
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)

    # exibir o gráfico
    grafico.show()


### Conclusões e Ações

# - A chance do cliente cancelar nos primeiros meses é muito alta
# - Isso pode significar que a gente está fazendo alguma promoção/a primeira experiência do cliente não está legal
# - Vamos fazer descontos nos primeios meses/dar bônus
# - Clientes com famílias maiores tendem a cancelar menos
# - Oferecer uma segunda linha de graça ou com desconto
# - Temos algum problema no serviço de fibra, a taxa de cancelamento está muito alta
# - Quanto mais serviços o cliente tem, menor a chance dele cancelar
# - Oferecer serviços de bônus ou com desconto
# - Oferecer um desconto para pagamento anual, quase todos os cancelamentos estão no mensal
# - Boleto tem muito mais cancelamento do que as outras formas
# - Dar desconto nas outras formas de pagamento
