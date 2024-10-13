# Nosso desafio é conseguir prever as vendas que vamos ter em determinado período com base nos gastos em anúncios nas 3 grandes redes que a empresa Hashtag investe: TV, Jornal e Rádio.
# Vendas estão em milhões
# Propagandas estão em milhares

import pandas as pd

tabela = pd.read_csv("advertising.csv")
display(tabela)

print(tabela.info())

display(tabela.corr())

import seaborn as sns
import matplotlib.pyplot as plt

# cria o gráfico
sns.heatmap(tabela.corr(), cmap="Wistia", annot=True)

# exibe o gráfico
plt.show()

# y -> é quem você quer prever

y = tabela["Vendas"]

# x -> quem eu vou usar para prever o y, ou seja, o resto da tabela

x = tabela[["TV", "Radio", "Jornal"]]

# Treinar com as informações e aprender a prever

from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1)

# importa ela
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# cria ela
modelo_regressaolinear = LinearRegression() # é o dos pontinhos, tenta traçar uma reta que explica seus dados
modelo_arvoredecisao = RandomForestRegressor() # modelo de perguntas para chegar a uma resposta

# treina ela
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

print("Modelos treinados")

from sklearn.metrics import r2_score

# fazer as previsões
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)
previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)

# comparar a previsão com o y_teste
print(r2_score(y_teste, previsao_arvoredecisao))
print(r2_score(y_teste, previsao_regressaolinear))

tabela_auxiliar = pd.DataFrame()
tabela_auxiliar['y_teste'] = y_teste
tabela_auxiliar["Previsão Regressão Linear"] = previsao_regressaolinear
tabela_auxiliar["Previsão Árvore decisão"] = previsao_arvoredecisao

plt.figure(figsize=(15, 5))
sns.lineplot(data=tabela_auxiliar)
plt.show()

tabela_nova = pd.read_csv("novos.atualizations.csv")
display(tabela_nova)

previsao = modelo_arvoredecisao.predict(tabela_nova)
print(previsao)