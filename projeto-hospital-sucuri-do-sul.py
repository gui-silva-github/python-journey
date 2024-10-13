import pandas as pd # importando a biblioteca pandas

import matplotlib.pyplot as plt # importando a biblioteca para gráficos

pg = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/dados_saude.csv') # importação dos dados

pg # print para ver a base de dados

pg = pg.drop('Unnamed: 0', axis = 1) # excluindo a coluna desnecessária criada

pg # print para ver a base de dados

pg.describe() # informações importantes sobre os dados, como ter 50000 linhas, a média, o desvio padrão, o mínimo e o máximo

pg.shape # sabendo o tamanho do  dataframe, nesse caso tem 50000 linhas e 5 colunas

pg.info() # sabendo as informações da base de dados, observa-se que todas  as saídas são do tipo float (flutuante)

# Histogramas

# Histograma da coluna "Peso":

pg.Peso.plot.hist(figsize = (15, 5), bins=30, grid = True)

# Histograma da coluna "Altura":

pg.Altura.plot.hist(figsize = (15, 5), bins=30, grid = True)

# Histograma da coluna "Idade":

pg.Idade.plot.hist(figsize = (15, 5), bins=30, grid = True)

# Sexualidades

pg.Sexo.value_counts() # para obter as quantidades

pg.Sexo.value_counts(normalize=True)*100 # para obter as porcentagens

# Tipos sanguíneos

pg.Tipo_Sangue.value_counts() # para obter as quantidades

pg.Tipo_Sangue.value_counts(normalize = True) * 100 # para obter as porcentagens

# Gráfico de Barras

pg.Sexo.value_counts().plot.bar(figsize = (10, 5)) # gráficos de barras dos sexos do usuário

pg.Tipo_Sangue.value_counts().plot.bar(figsize = (10, 5)) # gráficos de barras dos tipos sanguíneos dos usuários

# Criando a coluna IMC

pg['IMC'] = pg['Peso'] / (pg['Altura'] ** 2) # criando nova coluna do IMC

pg # printando a nova tabela de dados

# Determinando quantos usuários sofrem de obesidade grave

obesidade_grave = pg.query('IMC > 40.0') # criando a query

# Determinando se as pessoas que sofrem de “Magreza” têm uma distribuição do tipo sexo muito diferente dos usuários em geral.

magreza = pg.query('IMC < 18.5') # criando a query

magreza.head()

magreza.Sexo.value_counts() # para obter as quantidades

magreza.Sexo.value_counts(normalize=True)*100 # para obter as porcentagens

# Determinando se as pessoas que sofrem de “Obesidade grau 2” têm uma distribuição de tipo sanguíneo muito diferente dos usuários em geral.

obesidade_grauII = pg.query('IMC >= 30.0 & IMC <= 39.9') # criando a query

obesidade_grauII.head()

obesidade_grauII.Tipo_Sangue.value_counts() # para obter as quantidades

obesidade_grauII.Tipo_Sangue.value_counts(normalize=True)*100 # para obter as porcentagens

# Determinando quantas são as pessoas que sofrem ‘Magreza’ e quais são as médias de peso e idade desse grupo.

magreza.value_counts() # quantas pessoas sofrem de magreza

magreza.describe()

magreza.Peso.describe()

magreza.Idade.describe()

# Determinando o número do registro da mulher com mais peso entre as mulheres obesas grau 2.

obesas_grauII = pg.query('Sexo == 1.0 & IMC >= 30.0 & IMC <= 39.9') # criando a query

obesas_grauII.head()

obesas_grauII.describe() 

# Maior peso das obesas é de 89.54 kg, logo:

mais_obesa = pg.query('Sexo == 1.0 & Peso == 89.54') # criando a query

mais_obesa

# Fazendo uma análise comparando os histogramas com o peso das pessoas que sofrem de Magreza e dos usuários em geral.

# Histograma com o peso das pessoas que sofrem de Magreza:

magreza.Peso.plot.hist(figsize = (15, 5), bins=30, grid = True)

# Histograma com o peso dos usuários em geral:

pg.Peso.plot.hist(figsize = (15, 5), bins=30, grid = True)

# O IMC dos usuários em geral apresenta uma distribuição normal (gaussiana)?

pg.IMC.plot.hist(figsize=(10, 5), bins=30, grid=True)

pg.IMC.describe()