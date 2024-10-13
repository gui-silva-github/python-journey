print("********************************************************")
print("****BEM VINDO(A) AO ASSISTENTE PARA CÁLCULO DE MÉDIA****")
print("********************************************************")
print('')
print('')

i = 1 # contador
soma = 0
n = int(input('Entre com a quantidade de valores que você deseja calcular a média: '))
print('')
while (i <= n):
    print('Entre com um valor', i, ':')
    valor = int(input())
    i = i+1
    soma = soma + valor
    
media = soma/n
print('')
print('A média dos', n, 'valores é', media)