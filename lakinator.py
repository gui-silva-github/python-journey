import random

print('Jogo da Adivinhação')

# Condições iniciais
senha = ["x", "y", "z"]     # valores a serem adivinhados
vida = 3                    # Quantidade de Vidas. Pode ser alterado
pontos = 0                  # Pontuação começa zerada
rodada = 0                    # simples contador


# O JOGO EM SI
while (vida > 0):                    # Enquanto o jogador não morre...
  rodada = rodada + 1
  print('Bem vindo a rodada ', rodada)    # Exiba a rodada atual
  print('')
  valor = random.randrange(0,3)       # Gerando índice aleatório (de 0 a 2)
  chute = input("Adivinhe a senha digitando 'x', 'y' ou 'z': " )  #recebe chute

  if (chute == senha[valor]):       # Testa se chute é igual a senha da rodada
        # Se acertar execute esse bloco
    pontos = pontos + 200           # Incrementa pontuação
    print('Você acertou! Ganhou 200 pontos!') # mostra fase, pontos e vidas
    print('Você tem um total de', pontos, 'pontos')
    print('Você ainda tem ', vida, 'vida(s)')
    print('')
    # Se ainda tem vida, volte para o começo do while
  else:
        # Se errar execute esse bloco
    vida = vida - 1                # Perde uma vida se errar
    print('Você errou! A senha correta era ', senha[valor] ) # mostra senha correta
    print('Você tem um total de', pontos, 'pontos' ) # mostra pontos
    print('Você ainda tem ', vida, 'vida(s)')        # mostra vidas
    print('')
    # Se ainda tem vida, volte para o começo do while

# Saindo do While quando as vidas acabam
if (pontos == 0): # Se não fez nenhum ponto, mostre a mensagem abaixo
  print('Azarado! Você errou todas as vezes e não marcou pontos')

else:             # Se acertou pelo menos uma, mostre fase e pontuação abaixo
  print('')
  print('* Parabéns! Você sobreviveu a ', rodada, 'rodadas e marcou ', pontos, 'pontos *')
  print(' ')
print('')

print('Game Over')     # Fim de jogo