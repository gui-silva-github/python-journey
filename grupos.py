import random

lista = []

n = int(input("Digite a quantidade de nomes que você deseja colocar na lista? "))
contador = 0

while (contador < n):
  nome = input("Digite seu nome: ")
  lista.append(nome)
  contador = contador + 1
if n%2 == 0:
  qantdup = n/2
  random.shuffle(lista)
  dup = 0
  dup2 = 1
  cont = 0
  while cont < qantdup:
    print('A dupla é: ', lista[dup], ' e ', lista[dup2], sep='')
    dup = dup + 2
    dup2 = dup2 + 2
    cont = cont + 1
else:
  qantdup = (n-3) / 2
  random.shuffle(lista)
  print('O trio é: ' , lista[0], ', ', lista[1], ' e ', lista[2], sep='')
  dup = 3
  dup2 = dup2 + 2
  cont = cont + 1