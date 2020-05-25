# Escreva um programa que faça o computador "pensar" em um numero inteiro entra 0 e 5 e peça para o usuario tenta descobrir quela foi o numero escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
computador = randint(0, 5)
num = int(input('Em que numero estou pensando? '))
print('PROCESSANDO...')
sleep(3)
if computador == num:
    print('PARABENS! Voce acertou o numero {}'.format(computador))
else:
    print('GANHEI! Eu pensei no numero {} e não no {}'.format(computador, num))