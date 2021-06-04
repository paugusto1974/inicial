"""
Jogo Pedra, Papel e Tesoura
"""
# Importa função randint da biblioteca random
from random import randint
from time import sleep


# Função que retorna mensagem de PERDA
def perdeujogada(a):
    if a == 1:
        a = 'Pedra'
        b = 'Papel'
    elif a == 2:
        a = 'Papel'
        b = 'Tesoura'
    else:
        a = 'Tesoura'
        b = 'Pedra'
    tempojokenpo()
    print(f'\033[30;41m {a} PERDE de {b}')


# Função que retorna mensagem de GANHO
def ganhoujogada(a):
    if a == 1:
        a = 'Pedra'
        b = 'Tesoura'
    elif a == 2:
        a = 'Papel'
        b = 'Pedra'
    else:
        a = 'Tesoura'
        b = 'Papel'
    tempojokenpo()
    print(f'\033[30;43m {a} GANHA de {b}')


# Função para dar um tempo antes de apresentar o resultado
def tempojokenpo():
    print('JO-', end='')
    sleep(0.8)
    print('KEN-', end='')
    sleep(0.8)
    print('PO!')
    sleep(0.8)


# Valores iniciais de algumas variáveis
jogada = 4
perdeu = 0
ganhou = 0
empatou = 0
mensagem_erro = '\033[30;47m Opção Inválida! Tente novamente... '

# Evita que o programa seja finalizado até que o usuário decida encerrar
while jogada != 0:
    # Faz a jogada do computador escolhendo aleatoriamente um dos inteiros 1, 2 ou 3
    jkp = randint(1, 3)
    # Apresenta as possibilidades à escolha do usuário
    jogada = input('\033[30;46m [1] Pedra [2] Papel [3] Tesoura [0] Parar: \033[m ')
    if jogada.isnumeric():
        jogada = int(jogada)
    else:
        jogada = 4
        print(mensagem_erro)
        continue
    if jogada == jkp:
        tempojokenpo()
        print('\033[30;47m Empate! ')
        empatou = empatou + 1
    elif jogada == 1:
        if jkp == 2:
            perdeujogada(1)
            perdeu = perdeu + 1
        else:
            ganhoujogada(1)
            ganhou = ganhou + 1
    elif jogada == 2:
        if jkp == 3:
            perdeujogada(2)
            perdeu = perdeu + 1
        else:
            ganhoujogada(2)
            ganhou = ganhou + 1
    elif jogada == 3:
        if jkp == 1:
            perdeujogada(3)
            perdeu = perdeu + 1
        else:
            ganhoujogada(3)
            ganhou = ganhou + 1
    elif jogada != 0 != 1 != 2 != 3:
        print(mensagem_erro)
    else:
        print('\033[1m -=# Jogo Finalizado! #=- \033[m')
if perdeu != 0 or ganhou != 0:
    print(f'Você perdeu {perdeu}, ganhou {ganhou} e empatou {empatou} vezes.')
