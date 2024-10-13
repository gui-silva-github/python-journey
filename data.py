# importando o pandas

import pandas as pd

base = pd.read_csv('titanic_train.csv')

display(base)

# exibir o cabeçalho

base.head()

# visualizar as 5 últimas linhas * é um método

base.tail()

base.shape

display(base)

#  mostrando somente o tipo de dados
base.dtypes

# mostrando o tipo de dados e os valores vazios

base.info()

# contar os valores vazios por coluna

base.isnull().sum()

dados  =  {
    'X': [1,2,3, 3.6, 100]
}

dados = pd.DataFrame(dados)
display(dados)

# calculando a média

dados.mean()

# mostrando a contagem de registros

dados.count()

# mediana

dados.median()

# desvio padrão

dados.std()

# trazendo todo o resumo estatístico utilizando o describe

dados.describe()

# trazendo o resumo estatístico para a nossa base

base.describe()

# selecionando um conjunto de colunas

base[["Sex", "Age"]]

# verificando clientes que pagaram mais de 100 libras

base[base.Fare > 100]

# verificando clientes que pagaram menos de 5 libras

base[base.Fare < 5]

# verificando se alguém viajou com esposa E filhos

base[(base.Parch > 1) & (base.SibSp > 1)] # usar o And
base[(base.Parch > 1) | (base.SibSp > 1)].head() # usar o Ou

# usando o iloc

# buscando as linhas de 30 (inclusive) e 40 (exclusive)

base.iloc[30:40]

# também posso usar para buscar apenas colunas específicas
base.iloc[30:40, 3:6]

import matplotlib.pyplot as plt

# é possível fazer um histograma simples

base.Fare.hist(bins=20)

# gráfico de barras

base.Pclass.plot.bar()

base.Pclass.value_counts().plot.bar()

# E até gráficos mais complexos como o de densidade

base['Fare'].plot.kde()