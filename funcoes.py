def soma(a, b):
  resultado = a + b
  return resultado

x = soma(2, 3)
print(x)

# Crie uma função que ordena 3 valores na ordem crescente

def ordena3(x, y, z):
  if (x <= y and x <=z) : # supondo que x é o menor
    primeiro = x
    if (y <= z):
      segundo = y
      terceiro = z
    else:
      segundo = z
      terceiro = y
 
  if (y <= x and y <=z) : # supondo que y é o menor
    primeiro = y
    if (x <= z):
      segundo = x
      terceiro = z
    else:
      segundo = z
      terceiro = x

  if (z <= x and z <= y) : # supondo que z é o menor
    primeiro = z
    if (y <= x):
      segundo = y
      terceiro = x
    else:
      segundo = x
      terceiro = y

  return print(primeiro, segundo, terceiro)

ordena3(3, 2, 8)

# Crie uma função que recebe um n = a quantidade de dados e retorna a média dos dados

def media(n):
  i = 1
  soma = []
  while (i <= n):
    valor = int(input(f'''Entre com o valor {i}: '''))
    soma.append(valor)
    i += 1
  media = sum(soma)/n
  return media

print(media(3))

