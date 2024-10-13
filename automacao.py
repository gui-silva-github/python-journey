import automacao
import pyperclip
import time

automacao.PAUSE = 1

# Passo 1:
# Entrar no sistema da empresa (no nosso caso link do drive (https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga) )

automacao.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
automacao.hotkey("ctrl", "v")
automacao.press("enter")

time.sleep(5)

# Passo 2:
# Navegar no sistema e encontrar a base de vendas (entrar na pasta exportar)

automacao.click(x=413, y=277, clicks=2)
time.sleep(2)

# Passo 3:
# Fazer o dowload da Base de vendas

automacao.click(x=429, y=318) # clicar no arquivo
automacao.click(x=1162, y=158) # clicar nos 3 pontinhos
automacao.click(x=935, y=591) # clicar no fazer dowload

time.sleep(5)

# Passo 4:
# Importar a base de dados para o Python
import pandas as pd

tabela = pd.read_excel(r"C:\Users\Guilherme\Downloads\Vendas - Dez (5).xlsx")
display(tabela)

# Passo 5:
# Calcular os indicadores da empresa
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

print(faturamento)
print(quantidade)

# Passo 6:
# Enviar um e-mail para a diretoria com os indicadores de vendas

# abrir aba
pyautogui.hotkey("ctrl", "t")

# entrar no link do e-mail
pyperclip.copy("https://mail.google.com/mail/u/1/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)

# clicar no botão escrever
pyautogui.click(x=115, y=175)

# preencher as informações do e-mail
pyautogui.write("fulano@hotmail.com")
pyautogui.press("tab") # selecionar o e-mail

pyautogui.press("tab") # pular para o campo de assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab") # pular para o corpo do e-mail

texto = f"""
Prezados,

Segue o relatório de vendas:
Faturamento: R${faturamento:,.2f}
Quantidade de produtos vendidos: {quantidade:,.2f}

Qualquer dúvida estou a disposição.
Att.,
Guilherme Silva
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# enviar o e-mail
pyautogui.hotkey("ctrl", "enter")

### Usos:
# time.sleep(5) e pyautogui.position()