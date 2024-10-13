from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura') # nessa ordem 0, 1 e 2
computador = randint(0, 2) # o computador vai andar pelo "itens"

print("\033[31mBem vindo ao jogo do pedra, papel e tesoura!\033[0m ")
print('\u001b[34m-=' * 20)
print('\u001b[34m-=' * 20)
rod = int(input("Quantas rodadas iremos jogar? ")) # a quantidade de rodadas determinada pelo usuário

rodada = 0 # a rodada começa com 0 e será atualizada
contador = 0 # preparar a contagem para o while
pc = 0 # pontos do Pc
jogador = 0

while (contador < rod): # enquanto o contador que é 0 for menor do que a rod, faça isso:
  rodada += 1 # a mesma coisa que fazer rodada = rodada + 1
  print("""
  \033[31mRodada \033[0m""", rodada)
  print("\u001b[34m-=" * 20)
  jogada = int(input("""
  Entre com:
  0 - (Pedra)
  1 - (Papel)
  2 - (Tesoura)

  """))
  contador += 1
  print("\u001b[34m-=" * 20)
  print("JO")
  sleep(1)
  print("KEN")
  sleep(1)
  print("PÔ!!!")
  print("\u001b[34m-=" * 20)
  print("Computador jogou {}" .format(itens[computador]))
  print("\u001b[34m-=" * 20)
  print("Jogador jogou {}" .format(itens[jogada]))
  print("\u001b[34m-=" * 20)
  if computador == 0: # computador jogou Pedra
    if jogada == 0: # a jogada foi em Pedra
      print("EMPATE")
      pc += 1
      jogador += 1
      print(f"""O placar é de:
      Jogador X Computador
         {jogador}          {pc}
      """)
    elif jogada == 1: # a jogada foi em Papel
      print("""JOGADOR VENCEU:
      PAPEL EMBRULHA A PEDRA!
      """)
      pc += 0
      jogador += 1
      print(f"""O placar é de:
      Jogador X Computador
         {jogador}          {pc}
      """)
    elif jogada == 2: # a jogada foi em Tesoura
      print("""COMPUTADOR VENCEU:
      PEDRA QUEBRA A TESOURA!
      """"")
      pc += 1
      jogador += 0
      print(f"""O placar é de:
      Jogador X Computador
         {jogador}          {pc}
      """)
    else:
      print("Jogada inválida! ")
  elif computador == 1: # computador jogou Papel
    if jogada == 0: # a jogada foi em Pedra 
      print("""COMPUTADOR VENCEU:
      PAPEL EMBRULHA A PEDRA!
      """)
      pc += 1
      jogador += 0
      print(f"""O placar é de:
      Jogador X Computador
         {jogador}          {pc}
      """)
    elif jogada == 1: # a jogada foi em Papel
      print("EMPATE")
      pc += 1
      jogador += 1
      print(f"""O placar é de:
      Jogador X Computador
         {jogador}          {pc}
      """)
    elif jogada == 2: # a jogada foi em Tesoura
      print("""JOGADOR VENCEU:
      TESOURA CORTA O PAPEL!
      """)
      pc += 0
      jogador += 1
      print(f"""O placar é de:
      Jogador X Computador
         {jogador}          {pc}
      """)
    else:
      print("Jogada inválida! ") 
  elif computador == 2: # computador jogou Tesoura
    if jogada == 0: # a jogada foi em Pedra
      print("""JOGADOR VENCEU:
      PEDRA QUEBRA A TESOURA!
      """)
      pc += 0
      jogador += 1
      print(f"""O placar é de:
      Jogador X Computador
        {jogador}           {pc}
      """)
    elif jogada == 1:  # a jogada foi em Papel
      print("""COMPUTADOR VENCEU:
      TESOURA CORTA O PAPEL!
      """)
      pc += 1
      jogador += 0
      print(f"""O placar é de:
      Jogador X Computador
        {jogador}           {pc}
      """)
    elif jogada == 2:
      print("EMPATE")
      pc += 1
      jogador += 1
      print(f"""O placar é de:
      Jogador X Computador
        {jogador}           {pc}
      """)
    else:
      print("Jogada inválida! ")