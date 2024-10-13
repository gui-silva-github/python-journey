# Consulta de informações de um CEP

import requests

cep = "13300424"

cep = cep.replace("-", "").replace(".", "").replace(" ", "")

if len(cep) == 8:
    link = f'https://viacep.com.br/ws/{cep}/json/'
    requisicao = requests.get(link)
    
    print(requisicao)
    print(requisicao.json())


    dic_requisicao = requisicao.json()
    
    uf = dic_requisicao['uf']
    cidade = dic_requisicao['localidade']
    bairro = dic_requisicao['bairro']
    
    print(uf, cidade, bairro)

else:
    print("CEP inválido")

# Busca de um CEP a partir de um endereço

uf = "SP"
cidade = "São Paulo"
endereço = "Morumbi"

link = f'https://viacep.com.br/ws/{uf}/{cidade}/{endereço}/json/'

requisicao = requests.get(link)
print(requisicao)

dic_requisicao = requisicao.json()
print(dic_requisicao)