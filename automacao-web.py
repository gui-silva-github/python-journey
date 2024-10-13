# Passo 1: PEGAR A COTAÇÃO DO DÓLAR
# Passo 2: PEGAR A COTAÇÃO DO EURO
# Passo 3: PEGAR A COTAÇÃO DO OURO
# Passo 4: ATUALIZAR A BASE DE PREÇOS (atualizando o preço de compra e de venda)
# Passo 5: Exportar a base de preços atualizada

# Passo 1: PEGAR A COTAÇÃO DO DÓLAR
# abrir o navegador *
# entrar no google *
# pesquisar no google por 'cotacao dolar' *
# pegar a cotação que está no google *

from selenium import webdriver # permite criar o navegador
from selenium.webdriver.common.keys import Keys # permite você escrever no navegador
from selenium.webdriver.common.by import By # permite você selecionar itens no navegador

navegador = webdriver.Chrome() 

navegador.get("https://www.google.com/?safe=active&ssui=on")
navegador.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação Dólar")
navegador.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element("xpath", 
                                               '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_dolar)


# Passo 2: PEGAR A COTAÇÃO DO EURO
# abrir o navegador *
# entrar no google *
# pesquisar no google por 'cotacao dolar' *
# pegar a cotação que está no google *

from selenium import webdriver # permite criar o navegador
from selenium.webdriver.common.keys import Keys # permite você escrever no navegador
from selenium.webdriver.common.by import By # permite você selecionar itens no navegador

navegador = webdriver.Chrome() 

navegador.get("https://www.google.com/?safe=active&ssui=on")
navegador.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação Euro")
navegador.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element("xpath", 
                                               '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_euro)


# Passo 3: PEGAR A COTAÇÃO DO OURO *

navegador.get('https://www.melhorcambio.com/ouro-hoje')
cotacao_ouro = navegador.find_element("xpath", '//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(",", ".")

print(cotacao_ouro)


navegador.quit()


# Passo 4: ATUALIZAR A BASE DE PREÇOS (atualizando o preço de compra e de venda)

import pandas as pd

tabela = pd.read_excel("Produtos.xlsx")

# atualizar a coluna de cotação
# editar a coluna cotacao, onde a coluna moeda = dolar ou euro ou ouro

tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)

# atualizar a coluna de preço de compra = preco original * cotacao

tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]

# atualizar a coluna de preço de venda = preco de compra * margem

tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

display(tabela)

# Passo 5: Exportar a base de preços atualizada

tabela.to_excel("Produtos Novo.xlsx", index=False)