# Crie um programa que faça o computador jogar jokenpô com você (pedra, papel e tesoura)
from random import choice

print('-=-'*20)
print('                  Vamos jogar jokenpô!!')
print('-=-'*20)
jokenpo = str(input("pedra, papel ou tesoura? "))
lista = ['pedra', 'papel', 'tesoura']
computador = choice(lista)

if jokenpo == computador:
    print('Deu empate, ambos escolheram {}'.format(computador))
elif computador == 'pedra' and jokenpo == 'tesoura':
    print('Você escolheu {} e o computador {}, o computador ganhou!'.format(jokenpo, computador))
elif computador == 'tesoura' and jokenpo == 'papel':
    print('Você escolheu {} e o computador {}, o computador ganhou!'.format(jokenpo, computador))
elif computador == 'papel' and jokenpo == 'pedra':
    print('Você escolheu {} e o computador {}, o computador ganhou!'.format(jokenpo, computador))
else:
    print('Você escolheu {} e o computador {}, você ganhou!!'.format(jokenpo, computador))